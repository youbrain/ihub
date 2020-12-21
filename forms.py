from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class AddEventForm(FlaskForm):
    type = StringField("type: ", validators=[DataRequired()])

    photo = FileField(validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    time = StringField("time: ", validators=[DataRequired()])
    title = StringField("title: ", validators=[DataRequired()])
    description = TextAreaField("description: ", validators=[DataRequired()])

    submit = SubmitField("submit")
