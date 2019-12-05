#!/usr/bash/python3

from flask import Flask
from flask import redirect
from flask import url_for

@app.route("/bond")
def hello_bond():
    return "Hello Agent 007. Welcome back to M16"

@app.route("/login/<username")
    def login(username)
        if username == 007 or if username == "bond":
            return redirect(url_for("hello_bond"))
        else:
            return f"Welcome citizen. You do not have 00 clearance"

if __name__ == "__main__":
    app.run(port=5006)
