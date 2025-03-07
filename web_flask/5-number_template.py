#!/usr/bin/python3
"""
written by: yoseph-desalegn
cont:Write a script that starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def text(text):
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is_cool"):
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def temp_n(n):
    return render_template("5-number.html", value=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
