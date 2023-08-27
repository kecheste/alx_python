"""Importing flask package"""
from flask import Flask

app = Flask()
"""initializing flask app"""


@app.route('/')
def home():
    return "Hello HBNB!"


"""initializing basic routign"""
