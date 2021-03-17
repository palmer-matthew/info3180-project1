from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms.fields import StringField, TextAreaField, IntegerField, DecimalField, SelectField
from wtforms.validators import InputRequired, ValidationError

def length_check(max = -1):
    def length(form, field):
        if len(field.data) > max:
            raise ValidationError('Data is greater than {} characters'.format(max))    
    return length

def valid_number():
    def isInt(n):
        try:
            int(n)
        except:
            return False
        return True
    
    def isFloat(n):
        try:
            float(n)
        except:
            return False
        return True

    def check(form, field):
        if isInt(field.data) or isFloat(field.data):
            pass
        else:
            raise ValidationError('Value entered is not a valid integer or decimal') 
    return check



class PropertyForm(FlaskForm):
    
    title = StringField('Property Title', validators=[InputRequired(), length_check(max=145)])
    description = TextAreaField('Description', validators=[InputRequired(), length_check(max=255)])
    roomnum = StringField('No. of Rooms', validators=[InputRequired(), valid_number])
    bathnum = StringField('No. of Bathrooms', validators=[InputRequired(), valid_number])
    price = StringField('Price', validators=[InputRequired(), valid_number])
    type = SelectField('Property Type',validators=[InputRequired()], choices=[('House', 'House'), ('Apartment', 'Apt')])
    location = StringField('Location', validators=[InputRequired(), length_check(max=150)])
    photo = FileField('Photo Upload', validators= [FileRequired(), FileAllowed(['jpg','png','Images only!'])])