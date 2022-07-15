from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class RequestQouteForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Please Type Your Name")])
    email = StringField('Email', validators=[DataRequired(message="Please Type your email"), 
                        Email(message="please type a valid email")])
    website_name = StringField('Website')
    phone = StringField('Phone', validators=[DataRequired(message="Please Type your Phone number")])
    description = TextAreaField('Describe your inquirey!', validators=[DataRequired(message="Please Fill This Field")])

class ContactUsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Please Type Your Name")])
    email = StringField('Email', validators=[DataRequired(message="Please Type your email"), 
                        Email(message="please type a valid email")])
    website = StringField('Website')
    phone = StringField('Phone', validators=[DataRequired(message="Please Type your Phone number")])
    description = TextAreaField('Describe your inquirey!', validators=[DataRequired(message="Please Fill This Field")])

