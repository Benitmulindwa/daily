from flask import render_template, redirect, url_for, flash
from daily.forms import RegisterForm, LoginForm
from daily import app,db,bcrypt
import requests
from daily.models import User
from flask_login import login_user, logout_user, login_required

@app.route("/home")
@login_required
def home():
    response = requests.get("https://api.npoint.io/b26898f9241e01f827c6")
    data = response.json()
    return render_template("index.html", posts=data)

@app.route("/post/<int:id>")
@login_required
def blog(id):
    response = requests.get("https://api.npoint.io/b26898f9241e01f827c6")
    data = response.json()
    return render_template("post.html", post=data[id - 1])


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        newUser = User(

                       username=form.username.data,
                       email=form.email.data,
                       password=bcrypt.generate_password_hash(form.password1.data).decode("utf-8")

                       )
        
        db.session.add(newUser)
        db.session.commit()
        login_user(newUser)
        return redirect(url_for('home'))
    return render_template("users/register.html", form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email=form.email.data).first()
        if attempted_user and bcrypt.check_password_hash(attempted_user.password, form.password.data):
            login_user(attempted_user)
            flash(f"You have logged In successfully!", 'success')
            return redirect(url_for("home"))
        else:
             flash("Username and Password are not match!", 'danger')
    
    return render_template("users/login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("You have logged out successfully!", 'info')
    return redirect(url_for("login"))
