from app import app
from flask import render_template, flash , redirect , url_for

@app.route('/')
def hello():
 return render_template("html/home.html", title = 'Yeeet')
