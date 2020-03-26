from flask import Flask, jsonify, request
from main import start_hook


app = Flask(__name__)
script = start_hook()


@app.route("/auth/")
def auth():
    if not script:
        return jsonify({'error': 'please check frida...'})
    clienttype = request.args.get("clienttype")
    systemversion = request.args.get('systemversion')
    deviceUid = request.args.get('deviceUid')
    userLoginName = request.args.get('userLoginName')
    timestamp = request.args.get('timestamp')
    authentication = request.args.get('authentication')
    v = request.args.get("v")
    t = request.args.get("t")

    try:
        ret = script.exports.encrypt(clienttype, systemversion, deviceUid, userLoginName, timestamp, authentication, v, t)
    except Exception as e:
        ret = str(e)
    finally:
        return jsonify({"ret": ret})    


if __name__ == '__main__':
    app.run("")