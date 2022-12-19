"""
routes.py
Created: Sat Dec  3 12:13:14 CET 2022

It creates our 'home' blueprint. We define routes, templates and logic of the
homepage here. The home bluerprint is for web visitors. It guarantees
acces all free contents (i.e. blog, customization and forms).
"""
from flask import Blueprint, render_template

home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)

# note that every route must have a title and description
@home_bp.route("/")
def home():
    """Homepage visible to all users"""
    return render_template(
        "home.jinja2",
        title="Organostation App",
        description="Electrophysiology in a box",
    )


@home_bp.route("/test")
def test():
    """Test page"""
    return render_template("test.jinja2", title="test", description="simple test")


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
