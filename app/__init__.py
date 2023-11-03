from flask import Flask 

app = Flask(__name__)
app.secret_key = b"dwqdwqdwqdwqdw"

from app import views