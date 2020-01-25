from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField, BooleanField
from wtforms.validators import DataRequired, InputRequired
from local_events.routes import mongo

class CreateBandForm(FlaskForm):
    band_name = StringField('Band Name', validators=[DataRequired()])
    venue_name = SelectField(u'Venue', coerce=int, 
                            choices=([0, 'Please select a Venue'], [1, '02 Academy Sheffield'], [2, 'First Direct Arena'], [3, 'White Bear Barnsley'], [4, 'The Duchess York']), 
                            validators=[InputRequired()])
    event_date = DateTimeField('Gig Date', validators=[DataRequired()])
    is_headlining = BooleanField('Are They Headlining?', validators=[InputRequired()])
    band_logo = StringField('Band Logo')
    submit = SubmitField('Add Gig')

class CreateVenueForm(FlaskForm):
    venue_name = StringField('Venue Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    website = StringField('Venues Website')
    submit = SubmitField('Add Venue')
