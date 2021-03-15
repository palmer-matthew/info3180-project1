from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms.fields import StringField, TextAreaField, IntegerField, DecimalField, SelectField
from wtforms.validators import InputRequired, ValidationError

def length_check(max = -1):
    def length(form, field):
        if len(field.data) > max:
            raise ValidationError('Data is greater than {} characters'.format(max))    
    return length

class PropertyForm(FlaskForm):
    
    title = StringField('Property Title', validators=[InputRequired(), length_check(max=145)])
    description = TextAreaField('Description', validators=[InputRequired(), length_check(max=255)])
    roomnum = IntegerField('No. of Rooms', validators=[InputRequired()])
    bathnum = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    price = DecimalField('Price', places =2,validators=[InputRequired()])
    type = SelectField('Property Type',validators=[InputRequired()], choices=[('House', 'House'), ('Apartment', 'Apt')])
    location = StringField('Location', validators=[InputRequired(), length_check(max=150)])
    photo = FileField('Photo Upload', validators= [FileRequired(), FileAllowed(['jpg','png','Images only!'])])