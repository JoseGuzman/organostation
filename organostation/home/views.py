"""
views.py
Created: Sun Dec 25 21:10:17 CET 2022

It creates the routes (or views) for our 'home'. Home uses a
'home_bp' blueprint that define access to basic resources
from the home webpage.
We define routes, templates and logic of the homepage here.
"""
from flask import Blueprint, flash, redirect, render_template, url_for

from .forms import ContactForm, LoginForm, SignUpForm


def flash_errors(form):
    """Generate flash form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(
                "Error in %s field - %s" % (getattr(form, field).label.text, error),
                "error",
            )


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
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        print(f"Contact Form: {contact_form.data}")
        flash("Message sent successfully!")
        # Recreate form with no data to clean form #
        contact_form = ContactForm(formdata=None)
    else:
        print(f"Form Errors-> {contact_form.errors}")
        flash_errors(contact_form)  # check get_flashed_messages() in contact.jinja2

    return render_template(
        "contact.jinja2",
        title="Contact Us",
        description="Contact page",
        form=contact_form,
    )


@home_bp.route("/register", methods=["GET", "POST"])
def register():
    """Register page"""
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        print(f"Sign-up Form: {signup_form.data}")
        return redirect(url_for("home_bp.home"))
    else:
        print(f"Error-> {signup_form.errors}")
        flash_errors(signup_form)

    return render_template(
        "signup.jinja2", title="Register", description="Register page", form=signup_form
    )


@home_bp.route("/login", methods=["GET", "POST"])
def login():
    """Login page with username, password and remember me option"""
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(f"Contact Form: {login_form.data}")
        flash("Logged in successfully.")
        return redirect(url_for("home_bp.home"))
    else:
        print(f"Error-> {login_form.errors}")
        flash_errors(login_form)  # check get_flashed_messages() in login.jinja2

    return render_template(
        "login.jinja2", form=login_form, title="Login", description="Login Access"
    )


@home_bp.route("/configuration")
def configuration():
    """Technical specifications"""
    return render_template(
        "configuration.jinja2",
        title="Specifications",
        description="technical specifications",
    )


@home_bp.route("/test")
def test():
    """Test page"""
    return render_template("test.jinja2", title="Test Page", description="simple test")


@home_bp.route("/contact2")
def contact2():
    """Test page"""
    return render_template("contact.html", title="Test Page", description="simple test")
