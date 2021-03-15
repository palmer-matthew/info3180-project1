from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms.fields import StringField, TextAreaField, IntegerField, DecimalField, SelectField
from wtforms.validators import InputRequired

class PropertyForm(FlaskForm):
    
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    roomnum = IntegerField('No. of Rooms', validators=[InputRequired()])
    bathnum = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    price = DecimalField('Price', places =2,validators=[InputRequired()])
    type = SelectField('Property Type',validators=[InputRequired()], choices=[('House', 'House'), ('Apt', 'Apartment')])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo Upload', validators= [FileRequired(), FileAllowed(['jpg','png','Images only!'])])