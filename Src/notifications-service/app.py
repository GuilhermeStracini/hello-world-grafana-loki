import logging

from flask import Flask
from flask import request, jsonify


app = Flask(__name__)

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', encoding='utf-8', level=logging.INFO)



user_feedback = []

@app.route("/feedback", methods=["POST"])
def collect_feedback():
    feedback = request.json.get('feedback')
    user_feedback.append(feedback)
    return jsonify({'status': 'success', 'message': 'Feedback received'})
@app.route("/notifications", methods=["GET"])
def reservations():
    logging.info("Notifications endpoint")
    return "ok"
