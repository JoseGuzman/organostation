"""
forms.py
Created: Wed Dec 14 14:51:46 CET 2022

Determine the data our forms will handle, and whether a user has adquately completed a
form when they attempt to submit.
"""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    """ Contact form with name, email and body input fields and submit button"""
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    body = TextAreaField(
        "Message",
        validators=[DataRequired(), Length(min=4, message=('Your message is too short.'))
        ]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField("Submit")
