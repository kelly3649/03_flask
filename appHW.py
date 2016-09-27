import random
from flask import Flask, render_template, util.occupations
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Here is the starting page!"

@app.route("/occupations")
def mkTable():
    return render_template("occupations.html", dict=util.occupations.getPF(), RandOpp=util.occupations.randMan())

if __name__=="__main__":
    app.debug = True
    app.run()
