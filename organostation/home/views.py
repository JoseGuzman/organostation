"""
views.py
Created: Sun Dec 25 21:10:17 CET 2022

It creates the routes (or views) for our 'home'. Home uses a
'home_bp' blueprint that define access to basic resources
from the home webpage.
We define routes, templates and logic of the homepage here.
"""
from datetime import datetime as dtime

from flask import Blueprint, flash, redirect, render_template, session, url_for
from flask_login import current_user, login_required, login_user, logout_user

from .. import login_manager
from ..models import User, db
from .forms import ContactForm, LoginForm, SignUpForm


def flash_errors(form: dict):
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


@login_manager.user_loader
def load_user(user_id: str) -> User:
    """Flask-Login retrieves the ID of the user from the session"""
    return User.query.get(int(user_id))


@home_bp.before_request
def before_request():
    """Make sure we are connected to the database each time before a request."""
    session["_flashes"] = []  # clear flash information


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash("You must be logged in to view that page.")
    return redirect(url_for("home_bp.login"))


# =========================================================================
#  home
# =========================================================================
@home_bp.route("/")
@home_bp.route("/index.html")
def home():
    """The homepage will be visible to all users"""
    return render_template(
        "home.jinja2",  # uses layout and navigation jijna2 templates
        title="Organostation App",
        description="Electrophysiology in a box",
    )


# =========================================================================
#  contact
# =========================================================================
@home_bp.route("/contact", methods=["GET", "POST"])
def contact():
    """Contact form page"""
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        print(f"Contact Form: {contact_form.data}")
        flash("Message sent successfully!")
        # Recreate form with no data to clean form
        contact_form = ContactForm(formdata=None)
    else:
        print(f"Form Errors-> {contact_form.errors}")
        flash_errors(contact_form)  # get_flashed_messages() in contact.jinja2

    return render_template(
        "contact.jinja2",
        title="Contact Us",
        description="Contact page",
        form=contact_form,
    )


# =========================================================================
#  register
# =========================================================================
@home_bp.route("/register", methods=["GET", "POST"])
def register():
    """Register page"""
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for("home_bp.home"))

    signup_form = SignUpForm()
    if signup_form.validate_on_submit():  # POST validation
        print(f"Sign-up Form: {signup_form.data}")
        email = signup_form.data["email"]
        existing_user = User.query.filter(User.email == email).first()

        if existing_user:
            print(f"{existing_user} exists in Database")
            signup_form = SignUpForm(formdata=None)  # clear form
            flash(f"Error in Email: {email} already exists", "error")
        else:
            myuser = User(
                name=signup_form.name.data,
                surname=signup_form.surname.data,
                email=signup_form.email.data,
                created=dtime.utcnow(),
                admin=False,
            )
            myuser.set_password(signup_form.password.data)  # hash password
            db.session.add(myuser)
            db.session.commit()
            login_user(myuser)  # Log in as newly created user
            flash("User created successfully.")

            return redirect(url_for("home_bp.home"))

    else:
        print(f"Error-> {signup_form.errors}")
        flash_errors(signup_form)

    return render_template(
        "register.jinja2",
        title="Register",
        description="Register page",
        form=signup_form,
    )


# =========================================================================
#  login
# =========================================================================
@home_bp.route("/login", methods=["GET", "POST"])
def login():
    """Login page for registered users only.
    It contains username, password and remember me option"""

    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for("home_bp.home"))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(f"Contact Form: {login_form.data}")
        # login user is 'user_mail'
        myuser = User.query.filter_by(email=login_form.user_email.data).first()

        if myuser and myuser.check_password(password=login_form.password.data):
            login_user(myuser, remember=login_form.remember_me.data)
            flash("Logged in successfully.")
            return redirect(url_for("home_bp.home"))
        else:
            print("Invalid username or password")
            flash("Invalid username or password", "error")

        return redirect(url_for("home_bp.home"))
    else:
        print(f"Error-> {login_form.errors}")
        flash_errors(login_form)  # check get_flashed_messages() in login.jinja2

    return render_template(
        "login.jinja2", form=login_form, title="Login", description="Login Access"
    )


# =========================================================================
#  logout
# =========================================================================
@home_bp.route("/logout")
@login_required
def logout():
    """Logout page"""
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("home_bp.home"))


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
