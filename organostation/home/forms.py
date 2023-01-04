"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, InputRequired, Length


class ContactForm(FlaskForm):
    """Contact form with name, email and message."""

    name = StringField(label="Name", validators=[DataRequired(), Length(min=3)])
    email = StringField(
        label="Email",
        validators=[DataRequired(), Length(min=5), Email(granular_message=True)],
    )

    message = TextAreaField(
        label="Message",
        validators=[
            DataRequired(),
            Length(min=10, message=("The message is less than 10 chars.")),
        ],
    )
    # recaptcha = ecaptchaField()
    submit = SubmitField(label="Send Message")


class LoginForm(FlaskForm):
    """Login form with username and password."""

    user_mail = StringField(
        "User Email",
        validators=[DataRequired(), Length(min=5), Email(granular_message=True)],
    )
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("\t\n\r\x0b\x0c Remember me")
    submit = SubmitField("Log In")
