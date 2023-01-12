"""
views.py
Created: Sun Dec 25 21:10:17 CET 2022

It creates the routes (or views) for 'tutorials'. It uses 
'tutorial_bp' blueprint that define access to reserverd
lectures and resources.
We define routes, templates and logic of the homepage here.
"""

from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_required

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


# =========================================================================
# tutorials
# =========================================================================
@tutorials_bp.route("/home")
@login_required
def home():
    """Tutorials homepage"""
    return render_template(
        "tutorial.jinja2",  # uses layout and navigation jijna2 templates
    )


@tutorials_bp.route("/lectures/<int:lecture_id>")
@login_required
def lectures(lecture_id: int):
    """This links to the tutorial days"""
    print(f"you access day{lecture_id}")
    mytarget = f"day{lecture_id}/index.html"
    print(mytarget)
    return render_template(
        "lecture.jinja2", mytarget=mytarget
    )  # uses layout and navigation jijna2 templates
