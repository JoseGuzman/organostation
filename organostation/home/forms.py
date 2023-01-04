"""Form object declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    """Contact us form with name, email and body."""

    name = StringField("Name", validators=[DataRequired()])

    email = StringField(
        "Email",
        validators=[Email(message=("Not a valid email address.")), DataRequired()],
    )

    body = TextAreaField(
        "Message",
        validators=[
            DataRequired(),
            Length(min=4, message=("Your message is too short.")),
        ],
    )
    recaptcha = RecaptchaField()
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    """Login form with username and password."""

    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("\t\n\r\x0b\x0c Remember me")
    submit = SubmitField("Log In")
