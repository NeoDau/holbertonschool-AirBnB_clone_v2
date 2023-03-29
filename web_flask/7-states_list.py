#!/usr/bin/python3
""" shebang"""
from flask import Flask, render_template 
from models import storage
from models import State


app = Flask(__name__)


@app.teardown_appcontext
def close(x):
    """ call storage."""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    """ list in html"""
    return render_template("7-states_list.html", stt=storage.all("State").values())
    

if name == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
