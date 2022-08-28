from flask import Flask

import interface

app = Flask(__name__)


@app.route("/update/<int:id>")
def update(id: int) -> dict:
    return interface.update(id)


@app.route("/currentLyric/<int:id>")
def currentLyric(id: int) -> dict:
    return interface.getCurrentLyric(id)


if __name__ == "__main__":
    app.run()
