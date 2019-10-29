from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'reeeeevd'
from app import views