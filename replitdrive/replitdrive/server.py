import os
from flask import Flask, render_template
from settings import *

app = Flask("ReplitDrive")

@app.route("/")
def index():
    return render_template("index.html")

