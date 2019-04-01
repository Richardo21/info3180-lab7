from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators = [DataRequired()])
    photo = FileField('Select a photo', validators = [FileRequired(), FileAllowed(['jpg', 'png'],'Images Only!')])
