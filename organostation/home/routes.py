"""
routes.py
Created: Sat Dec  3 12:13:14 CET 2022

It creates our 'home' blueprint. We define routes, templates and logic of the
homepage here. Visitors will have access to all contents of home.
"""
from flask import Blueprint
from flask import current_app as app
from flask import render_template

home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route("/")
def index():
    """Homepage"""
    return render_template(
        "home.jinja2", title="Organostation", subtitle="Electrophysiology in a box"
    )


@home_bp.route("/test")
def test():
    """This is a test page"""
    return render_template("test.html", description="simple test", info=42)


@home_bp.route("/tutorials")
def tutorials():
    """open list of tutorials"""
    return render_template("tutorials.html")


@home_bp.route("/customise")
def customise():
    """customise page"""
    return render_template("customise.html")


@home_bp.route("/login", methods=["GET", "POST"])
def login():
    """
    The Login form
    """
    loginform = LoginForm()

    if loginform.validate_on_submit():
        return "It's valid"

    return render_template("login.html", form=loginform)


@home_bp.route("/register", methods=["GET", "POST"])
def register():
    """
    The Register opens a new page with a form
    """
    registerform = RegistrationForm()

    if registerform.validate_on_submit():
        return "It's valid"

    return render_template("register.html", form=registerform)


@home_bp.route("/logout")
def logout():
    """when logout, go to index"""
    return render_template("index.html")
