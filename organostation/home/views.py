"""
views.py
Created: Sun Dec 25 21:10:17 CET 2022

It creates the routes (or views) for our 'home'. Home uses a 
'home_bp' blueprint that define access to basic resources
from the home webpage. 
We define routes, templates and logic of the homepage here. 
"""
from flask import Blueprint, render_template

from .forms import ContactForm, LoginForm

home_bp = Blueprint(
    "home_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/home",  # local static content
)


@home_bp.route("/")
def home():
    """The homepage will be visible to all users"""
    return render_template(
        "home.jinja2",  # uses layout and navigation jijna2 templates
        title="Organostation App",
        description="Electrophysiology in a box",
    )


@home_bp.route("/contact", methods=["GET", "POST"])
def contact():
    """Contact form page"""
    myform = ContactForm()
    if myform.validate_on_submit():
        return redirect(url_for("home_bp.home"))

    return render_template(
        "contact.jinja2", title="Contact Us", description="Contact page", form=myform
    )


@home_bp.route("/configuration")
def configuration():
    """Technical specifications"""
    return render_template(
        "configuration.jinja2",
        title="Specifications",
        description="technical specifications",
    )


@home_bp.route("/register")
def register():
    """Register page"""
    return render_template(
        "register.html", title="Register", description="Register page"
    )


@home_bp.route("/login", methods=["GET", "POST"])
def login():
    """Login page with username, password and remember me option"""
    myform = LoginForm()
    if myform.validate_on_submit():
        return redirect(url_for("home_bp.home"))

    return render_template(
        "login.jinja2", form=myform, title="Login", description="Login Access"
    )


@home_bp.route("/test")
def test():
    """Test page"""
    return render_template("test.jinja2", title="Test Page", description="simple test")


@home_bp.route("/contact2")
def contact2():
    """Test page"""
    return render_template("contact.html", title="Test Page", description="simple test")
