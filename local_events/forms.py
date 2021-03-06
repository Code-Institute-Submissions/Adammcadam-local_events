from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, InputRequired
from wtforms.fields.html5 import DateField
from local_events import mongo

class CreateBandForm(FlaskForm):
    band_name = StringField('Band Name', validators=[DataRequired()])
    band_logo = StringField('Band Logo')
    submit = SubmitField('Post')

class CreateVenueForm(FlaskForm):
    venue_name = StringField('Venue Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    website = StringField('Venues Website')
    submit = SubmitField('Post')
