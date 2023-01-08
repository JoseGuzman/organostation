"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class ContactForm(FlaskForm):
    """Contact form with name, email and message."""

    name = StringField(label="Name", validators=[DataRequired(), Length(min=3)])
    email = StringField(
        label="Email",
        validators=[DataRequired(), Length(min=6), Email(granular_message=True)],
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
        label="User Email",
        validators=[DataRequired(), Length(min=6), Email(granular_message=True)],
    )
    password = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            Length(min=8, message="Password must be at least 8 characters long"),
        ],
    )
    remember_me = BooleanField("\t\n\r\x0b\x0c Remember me")
    submit = SubmitField("Log In")


class SignUpForm(FlaskForm):
    """Sign up from with name, surname, email, password and confirm password ."""

    name = StringField(label="Name", validators=[DataRequired(), Length(min=3)])
    surname = StringField(label="Surname", validators=[DataRequired(), Length(min=3)])
    email = StringField(
        label="Email",
        validators=[DataRequired(), Length(min=6), Email(granular_message=True)],
    )

    password = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            Length(min=8, message="Password must be at least 8 characters long."),
        ],
    )

    confirm = PasswordField(
        label="Confirm Your Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    terms = BooleanField("\t\n\r\x0b\x0c I agree to the terms and conditions.")

    submit = SubmitField("Register")
