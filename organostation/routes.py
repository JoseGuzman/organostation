"""
routes.py
Created: Sat Dec  3 12:13:14 CET 2022

Flask routes declaration file
"""
from flask import current_app as app
from flask import render_template


@app.route("/")
def home():
    """home page for OrganoStation"""
    return render_template(
        "home.html",
        title="OrganoStation",
        info="A visualisation app to document electrical or fluorescence signals.",
    )


@app.route("/test")
def test():
    """This is a test page"""
    return render_template("test.html", description="simple test", info=42)


@app.route("/")
def index():
    """main page"""
    return render_template("index.html")


@app.route("/tutorials")
def tutorials():
    """open list of tutorials"""
    return render_template("tutorials.html")


@app.route("/customise")
def customise():
    """customise page"""
    return render_template("customise.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    The Login form
    """
    loginform = LoginForm()

    if loginform.validate_on_submit():
        return "It's valid"

    return render_template("login.html", form=loginform)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    The Register opens a new page with a form
    """
    registerform = RegistrationForm()

    if registerform.validate_on_submit():
        return "It's valid"

    return render_template("register.html", form=registerform)


@app.route("/logout")
def logout():
    """when logout, go to index"""
    return render_template("index.html")
