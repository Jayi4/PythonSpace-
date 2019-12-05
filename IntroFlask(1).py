#!/usr/bash/python3

from flask import Flask

#The "flask" you are actually acting on its the "Flask" after the 'import' commmand. Be sure to verify case sensitivity
app = Flask(__name__)

@app.route("/")
def hola_mundo():
    x = 1
    y = 2
    return f"The results of {x} plus {y} is equal to {x +y}"

@app.route("/bond")
def bond():
    return f"Bond, James Bond 007"

@app.route("/secretagent/<donumber>")
def britishagent(donumber):
    return f"Hello Secret Agent {donumber}. We have an assignment for you"


if __name__ == "__main__":
    app.run(port=5066)


#flask: automation tool framework. Simply put: "A way to make code highly available"