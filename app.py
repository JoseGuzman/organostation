"""
app.py

Main App application

Jose Guzman, sjm.guzman@gmail.com
Created: Fri Aug 12 19:37:32 EDT 2022

# Run this app with pipenv shell and type `flask run` and
# visit http://127.0.0.1:8051/ in your web browser.
"""
#from unicodedata import name
# basic Flask
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

# forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, Email

# database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# dashboard
# from dashboards.visualoid import create_dashboard, test_layout
from dashboards import testboard

app = Flask(__name__)
app.config["SECRET_KEY"] = b'_5#y2L"F4Q8z\n\xec]/'
Bootstrap(app)  # we bootstrap our application

# database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"  # database location
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ==========================================================================
# dashboards
# ==========================================================================
#testboard.simple_callback(flask_app = app)
testboard.test_layout(flask_app=app)
# test_layout(flask_app = app)


class LoginForm(FlaskForm):
    """ user/pass login"""
    email = StringField("E-mail", validators=[Email()])
    passwd = PasswordField("Password", validators=[Length(min=8)])


class RegistrationForm(FlaskForm):
    """ registration involves name and institution/company """
    name = StringField("First name", validators=[Length(min=4, max=20)])
    surname = StringField("Last name", validators=[Length(min=4, max=20)])
    email = StringField("E-mail", validators=[Email()])
    passwd = PasswordField("Password", validators=[Length(min=8)])
    passwd2 = PasswordField("Confirm password", validators=[Length(min=8)])
    project = StringField("Brief project description",
                          validators=[Length(max=280)])

# Models are to map tables in db to python objects


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    surname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    passwd = db.Column(db.String(128), nullable=False)
    project = db.Column(db.String(280))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tutorials")
def tutorials():
    """ open list of tutorials """
    return render_template("tutorials.html")


@app.route("/customise")
def customise():
    """ customise page """
    return render_template("customise.html")


@app.route("/test")
def test():
    """ for testing only """
    return render_template("test.html")


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
    """ when logout, go to index"""
    return render_template(url_for('index'))


if __name__ == "__main__":
    # if using python app.py you need environment
    app.run(debug=True, port=8051)  # export FLASK_DEBUG=1
