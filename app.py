from flask import Flask

from utils.logics import factorial


app  = Flask(__name__)


@app.route("/<int:number>", methods=["GET"])
def calculate(number: int):
    return {"result": factorial(number)}


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
