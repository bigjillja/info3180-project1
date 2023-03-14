from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    property_type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    bedrooms = StringField('No. of Bedrooms', validators=[DataRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators=[DataRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
