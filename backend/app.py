from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from data_fetch import fetch_data
from detection import detect_anomalies
from classification import classify_events

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/fetch', methods=['GET'])
def fetch():
    data = fetch_data()
    return jsonify(data)

@app.route('/detect', methods=['GET'])
def detect():
    anomalies = detect_anomalies()
    return jsonify(anomalies)

@app.route('/classify', methods=['GET'])
def classify():
    events = classify_events()
    socketio.emit('new_event', events)
    return jsonify(events)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
