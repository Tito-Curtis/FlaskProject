from market import app
from flask import render_template,redirect,url_for,flash
from market.models import Item,User
from market.forms import RegisterForm,LoginForm
from market import db
from flask_login import login_user,logout_user,login_required


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/market')
@login_required
def market():
    item=Item.query.all()
    
    return render_template('market.html', item=item)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=(form.username.data).lower(),
                         email_address=(form.email_address.data).lower(),
                         password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        
        return redirect(url_for('market'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html',form=form)

@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            
            return redirect(url_for('market'))
        else:
            flash('Username and Password do not match', category='danger')

    return render_template('login.html',form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))