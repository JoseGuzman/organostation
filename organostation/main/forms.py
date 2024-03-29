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
    """User_email and password to simply log In."""

    user_email = StringField(
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
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Log In")


class SignUpForm(FlaskForm):
    """Sign up from with name, surname, email, password and confirm password."""

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

    terms = BooleanField(
        label="\t\n\r\x0b\x0c I agree to the terms and conditions.",
        validators=[
            DataRequired(message="You must agree to the terms and conditions.")
        ],
    )

    submit = SubmitField("Register")


class UpdateAccountForm(FlaskForm):
    """Update database name or surname, or add
    phone, address1, address2, and postcode"""

    name = StringField(label="Name", validators=[Length(min=3)])
    surname = StringField(label="Surname", validators=[Length(min=3)])

    phone = StringField(label="Phone", validators=None)
    address1 = StringField(label="Address 1", validators=None)
    address2 = StringField(label="Address 2", validators=None)
    postcode = StringField(label="Postcode", validators=None)
    city = StringField(label="City", validators=None)
    country = StringField(label="Country", validators=None)

    submit = SubmitField("Update Profile")
