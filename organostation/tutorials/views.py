"""
views.py
Created: Sun Dec 25 21:10:17 CET 2022

It creates the routes (or views) for 'tutorials'. It uses 
'tutorial_bp' blueprint that define access to reserverd
lectures and resources.
We define routes, templates and logic of the homepage here.
"""
from datetime import datetime as dtime

from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from .. import login_manager
from ..models import User

tutorials_bp = Blueprint(
    "tutorials_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/tutorials",  # local static content
)


@login_manager.user_loader
def load_user(user_id: str) -> User:
    """Flask-Login retrieves the ID of the user from the session"""
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash("You must be logged in to view that page.")
    return redirect(url_for("home_bp.login"))


# add to all footer.jinja2
@tutorials_bp.context_processor
def inject_now():
    """makes 'now' available to all templates"""
    return {"now": dtime.utcnow()}


# =========================================================================
# tutorials
# =========================================================================
@tutorials_bp.route("/tutorials")
@login_required
def home():
    """Tutorials homepage"""
    return render_template(
        "tutorial_copy.jinja2",
        title="Tutorials",  # uses layout and navigation jijna2 templates
    )


@tutorials_bp.route("/tutorial/<int:lecture_id>")
@login_required
def tutorial(lecture_id: int):
    """This links to the tutorial days"""
    if current_user.client is False:
        mytitle = "Access Denied"
        mymmsg = "Tutorials are part of the exclusive support we provide to our scientist.<br/> Please <a href='contact'>Contact Us</a> to guarantee you access."
        return (render_template("errors.jinja2", title=mytitle, message=mymmsg), 403)
    else:
        print(f"you access day{lecture_id}")
        mytarget = f"day{lecture_id}/index.html"
        print(mytarget)
        return render_template(
            "lecture.jinja2", title=lecture_id, mytarget=mytarget
        )  # uses layout and navigation jijna2 templates
