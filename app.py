"""
app.py

Main App application

Jose Guzman, sjm.guzman@gmail.com
Created: Fri Aug 12 19:37:32 EDT 2022

"""
from unicodedata import name
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, Email

app = Flask(__name__, template_folder = "templates")
app.config["SECRET_KEY"] = "foo"

Bootstrap(app)

class LoginForm(FlaskForm):
    email = StringField("E-mail", validators = [ Email() ])
    passwd = PasswordField("Password", validators = [ Length(min=8) ] )

class RegistrationForm(FlaskForm):
    name = StringField("Username", validators = [ Length(min=4, max =20) ])
    email = StringField("E-mail", validators = [ Email() ])
    passwd = PasswordField("Password", validators = [ Length(min=8) ] )
    passwd2 = PasswordField("Confirm password", validators = [ Length(min=8) ] )
     

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    """
    The Login form
    """
    loginform = LoginForm()

    if loginform.validate_on_submit():
        return "It's valid"

    return render_template("login.html", form = loginform)

@app.route("/register", methods = ["GET", "POST"])
def register():
    """
    The Register form
    """
    registerform = RegistrationForm()

    if registerform.validate_on_submit():
        return "It's valid"

    return render_template("register.html", form = registerform)

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run()
