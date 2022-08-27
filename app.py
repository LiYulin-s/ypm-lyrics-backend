from flask import Flask

import interface

from interface import *

app = Flask(__name__)
@app.route("/update/<int:id>")
def update(id:int):
    return interface.update(id)

@app.route("/currentLyric/<int:id>")
def currentLyric(id:int):
    json = interface.getCurrentLyric(id)
    return json

if __name__ == "__main__" :
    app.run()