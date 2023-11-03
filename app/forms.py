from flask_wtf import FlaskForm
from wtforms import StringField

class MessageForm(FlaskForm):
    username = StringField("Ваше ім'я")
    message = StringField("Ваше повідомлення")