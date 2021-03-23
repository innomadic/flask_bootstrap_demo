from flask import render_template
from app import app


@app.route('/')
def hello():
    return render_template('base.html', title='Home', user='nick')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

@app.route('/flavors')
def flavors():
    flavors = ["strawberry", "mango", "chocolate"]
    return render_template('flavors.html', title='Flavors', user='nick', flavors=flavors)