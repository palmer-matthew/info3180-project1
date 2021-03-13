from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms.fields import StringField, TextAreaField, IntegerField, FloatField, SelectField
from wtforms.validators import InputRequired
from wtforms.widgets.core import Input

class PropertyForm(FlaskForm):
    
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    roomnum = IntegerField('Number of Rooms', validators=[InputRequired()])
    bathnum = IntegerField('Number of Bathrooms', validators=[InputRequired()])
    price = FloatField('Price', validators=[InputRequired()])
    type = SelectField('Property Type',validators=[InputRequired()], choices=[('House', 'House'), ('Apt', 'Apartment')])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo Upload', validators= [FileRequired(), FileAllowed(['jpg','png','Images only!'])])