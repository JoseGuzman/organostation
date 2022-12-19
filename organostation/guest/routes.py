"""
routes.py
Created: Sat Dec  3 12:13:14 CET 2022

It creates the routes (or views) for our 'guests'. Guest use a 
'guest_bp' blueprint that define access to the list of resources
indicated in this script. 
We define routes, templates and logic of the
homepage here. 
"""
from flask import Blueprint, render_template, redirect, url_for
from .forms import ContactForm

guest_bp = Blueprint(
    "guest_bp", __name__, template_folder="templates", static_folder="static"
)

# note that every route must have a title and description
@guest_bp.route("/")
def home():
    """Homepage visible to all users"""
    return render_template(
        "home.jinja2",
        title = "Organostation App",
        description = "Electrophysiology in a box"
    )

@guest_bp.route("/specs")
def specs():
    """Technical specifications"""
    return render_template(
        "specs.jinja2",
        title = "Specifications",
        description = "technical specifications"
    )

@guest_bp.route("/test")
def test():
    """Test page"""
    return render_template(
        "test.jinja2", 
        title="test", 
        description="simple test"
    )


@guest_bp.route("/contact", methods=["GET", "POST"])
def contact():
    """Contact form"""
    myform = ContactForm()
    if myform.validate_on_submit():
        return redirect( url_for("guess_bp.success") )

    return render_template(
        "contact.jinja2",
        form = myform,
        title = "Contact form",
        description = "Contact form"
    )

@guest_bp.route("/customise")
def customise():
    """customise page"""
    return render_template("customise.html")


@guest_bp.route("/login", methods=["GET", "POST"])
def login():
    """
    The Login form
    """
    loginform = LoginForm()

    if loginform.validate_on_submit():
        return "It's valid"

    return render_template("login.html", form=loginform)


@guest_bp.route("/register", methods=["GET", "POST"])
def register():
    """
    The Register opens a new page with a form
    """
    registerform = RegistrationForm()

    if registerform.validate_on_submit():
        return "It's valid"

    return render_template("register.html", form=registerform)


@guest_bp.route("/logout")
def logout():
    """when logout, go to index"""
    return render_template("index.html")
