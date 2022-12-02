from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, RadioField, SelectField, URLField
from wtforms.validators import InputRequired, Optional, NumberRange, ValidationError


class PetForm(FlaskForm):
    def valid_bool(form, field):
        if field.data != 'True' and field.data != 'False':
            raise ValidationError(
                'this is a custon error only True False Values allowed!')

    name = StringField('Pet Name', validators=[InputRequired()])
    pet_species = SelectField('Species', validators=[InputRequired()])
    photo_url = URLField('Photo URL', validators=[Optional()])
    age = IntegerField('Age', validators=[
                       InputRequired(), NumberRange(min=0, max=30)])
    notes = StringField('Notes')
    available = SelectField("Adoption Status", choices=[("True", 'Available'), (
        "False", 'Unavailable')], validators=[valid_bool])


class AddSpeciesForm(FlaskForm):

    species_id = StringField('Species id', validators=[
        InputRequired(message='must be a unique species id')])
    species_name = StringField('Species name', validators=[
        InputRequired(message='must be a unique species name')])
