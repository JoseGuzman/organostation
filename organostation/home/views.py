"""
views.py
Created: Sun Dec 25 21:10:17 CET 2022

It creates the routes (or views) for our 'home'. Home uses a 
'home_bp' blueprint that define access to basic resources
from the home webpage. 
We define routes, templates and logic of the homepage here. 
"""
from flask import Blueprint, render_template

home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route("/")
def home():
    """Homepage visible to all users"""
    return render_template(
        "home.jinja2",  # global template
        title="Organostation App",
        description="Electrophysiology in a box",
    )


@home_bp.route("/test")
def test():
    """Test page"""
    return render_template("test.jinja2", title="Test Page", description="simple test")


@home_bp.route("/specs")
def specs():
    """Technical specifications"""
    return render_template(
        "home.jinja2", title="Specifications", description="technical specifications"
    )


@home_bp.route("/register")
def register():
    """Register page"""
    return render_template("home.jinja2", title="Register", description="Register page")


@home_bp.route("/login")
def login():
    """Login page"""
    return render_template("login.html", title="Register", description="Register page")
