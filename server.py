from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/b26898f9241e01f827c6")
    data = response.json()
    return render_template("index.html", posts=data)


@app.route("/post/<int:id>")
def blog(id):
    response = requests.get("https://api.npoint.io/b26898f9241e01f827c6")
    data = response.json()
    return render_template("post.html", post=data[id])


if __name__ == "__main__":
    app.run(debug=True)
