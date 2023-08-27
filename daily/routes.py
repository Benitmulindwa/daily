from flask import render_template, request,redirect,url_for
from daily.forms import RegisterForm
from daily import app,db
import requests
from daily.models import User

@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/b26898f9241e01f827c6")
    data = response.json()
    return render_template("index.html", posts=data)


@app.route("/post/<int:id>")
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
                       password=form.password1.data

                       )
        
        db.session.add(newUser)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template("users/register.html", form=form)
