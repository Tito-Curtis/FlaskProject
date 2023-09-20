from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/market')
def market():
    item=Item.query.all()
    
    return render_template('market.html', item=item)

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html')



