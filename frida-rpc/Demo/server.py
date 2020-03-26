from flask import Flask, jsonify, request
from demo import start_hook


app = Flask(__name__)
script = start_hook()


@app.route("/calculate")
def calculate():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = script.exports.add(a, b)
    return jsonify({"result": result})    


if __name__ == '__main__':
    app.run("0.0.0.0", 80)

