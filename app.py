import os
from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Get Webex access token and port from environment variables
WEBEX_ACCESS_TOKEN = os.environ.get("WEBEX_ACCESS_TOKEN")
PORT = int(os.environ.get("PORT", 5000))  # Default to 5000 if not set

if not WEBEX_ACCESS_TOKEN:
    raise ValueError("WEBEX_ACCESS_TOKEN is not set in environment variables.")

WEBEX_API_URL = "https://webexapis.com/v1"

headers = {
    "Authorization": f"Bearer {WEBEX_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

@app.route("/", methods=["POST"])
def webex_webhook():
    data = request.json

    if not data:
        return "Invalid request", 400

    logging.info("Webhook payload received:")
    logging.info(data)

    message_id = data.get("data", {}).get("id")
    if message_id:
        message = get_message_details(message_id)
        if message:
            logging.info(f"Message text: {message.get('text')}")
        else:
            logging.warning("Could not fetch message details.")

    return jsonify({"status": "message received", "receviedMessage": message.get('text')}), 200

def get_message_details(message_id):
    try:
        response = requests.get(
            f"{WEBEX_API_URL}/messages/{message_id}",
            headers=headers
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching message: {e}")
        return None

if __name__ == "__main__":
    app.run(port=PORT, debug=True)