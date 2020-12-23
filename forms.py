from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class AddEventForm(FlaskForm):
    type = StringField("Тип заходу (воркшоп, хакатон, лекція): ", validators=[DataRequired()])

    photo = FileField('Фото: ' ,validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], "Тільки 'jpg', 'png' розширення")
    ])
    time = StringField("Дата початоку (08-07-2002 16:00): ", validators=[DataRequired()])
    title = StringField("Заголовок: ", validators=[DataRequired()])
    description = TextAreaField("Опис: ", validators=[DataRequired()])

    submit = SubmitField("Додати івент")
