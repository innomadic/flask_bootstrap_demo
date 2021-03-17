from flask import render_template
from app import app


@app.route('/')
def hello():
    flavors = ["vanilla", "chocolate"]
    return render_template('base.html', title='Home', user='nick', flavors=flavors)
