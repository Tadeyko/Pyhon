from app import app
from flask import render_template, flash, redirect, url_for
from .forms import MessageForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    message = db.Column(db.String(300))

@app.route('/', methods=['GET', 'POST'])
def home():
    form = MessageForm()
    messages = db.session.query(Message).all()

    if form.validate_on_submit():
        username = form.username.data
        message = form.message.data

        new_message = Message(username=username, message=message)
        db.session.add(new_message)
        db.session.commit()

        flash("Ваше повідомлення було додано")
        
        return redirect(url_for("home"))

    return render_template('index.html', form=form, messages=messages)