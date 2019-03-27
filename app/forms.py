from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf import FlaskForm
from flask_wtf import TextAreaField, validators

class UploadForm(FlaskForm):
    description = TextAreaField('Description', [validators.DataRequired()])
    photo = FileField('Select a photo', validators = [FileRequired(), FileAllowed(['jpg', 'png'],'Images Only!')])
