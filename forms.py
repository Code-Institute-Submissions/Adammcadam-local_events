from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length, InputRequired, URL

class CreateBandForm(FlaskForm):
    band_name = StringField('Your Bands Name', validators=[DataRequired()])
    venue_name = StringField('Where are you playing?', validators=[DataRequired()])
    is_headlining = BooleanField('Are you headlining?')
    event_date = DateTimeField('When are you playing?', validators=[InputRequired()])
    band_logo = StringField('Image Link (full path)', validators=[DataRequired()])
    submit = SubmitField('Add Band')
    
class EditBandForm(FlaskForm):
    band_name = StringField('Your Bands Name', validators=[DataRequired()])
    venue_name = StringField('Where are you playing?', validators=[DataRequired()])
    is_headlining = BooleanField('Are you headlining?')
    event_date = DateTimeField('When are you playing?', validators=[InputRequired()])
    band_logo = StringField('Image Link (full path)', validators=[DataRequired()])
    submit = SubmitField('Edit Band')
    
class ConfirmCompletion(FlaskForm):
    submit = SubmitField('Complete Event')