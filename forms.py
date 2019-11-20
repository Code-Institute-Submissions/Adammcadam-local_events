from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length, InputRequired, URL

class CreateBandForm(FlaskForm):
    band_name = StringField('Band Name', validators=[DataRequired()])
    venue_name = StringField('Venue', validators=[DataRequired()])
    is_headlining = BooleanField('Are you headlining?')
    event_date = DateTimeField('Event Date', validators=[InputRequired()])
    band_logo = StringField('Image Link (full path)', validators=[DataRequired()])
    submit = SubmitField('Add Band')
    
class EditBandForm(FlaskForm):
    band_name = StringField('Band Name', validators=[DataRequired()])
    venue_name = StringField('Venue', validators=[DataRequired()])
    is_headlining = BooleanField('Are you headlining?')
    event_date = DateTimeField('Event Date', validators=[InputRequired()])
    band_logo = StringField('Image Link (full path)', validators=[DataRequired()])
    submit = SubmitField('Edit Band')
    
class ConfirmCompletion(FlaskForm):
    submit = SubmitField('Complete Event')

class CreateVenueForm(FlaskForm):
    venue_name = StringField('Name', validators=[DataRequired()])
    venue_desc = StringField('Description', validators=[DataRequired()])
    venue_website = StringField('URL', validators=[DataRequired()])
    venue_location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Add Venue')