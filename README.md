# Webex Webhook Test Server

This is a lightweight Flask application that receives and processes incoming [Webex](https://developer.webex.com/) webhook messages. It logs incoming message details and fetches the full message content using the Webex API.

## Features

- Listens for Webex webhook POST requests
- Fetches full message content using Webex API
- Logs message ID, sender, room, and text
- Loads sensitive configuration from environment variables

---

## Requirements

- Python 3.7+
- Webex Bot Access Token
- Flask
- Requests

Install dependencies:

```bash
pip install flask requests
```

## Docker 
You can run this application via Docker
    - `WEBEX_ACCESS_TOKEN` : is required to pull message detail from webex. 
    - `PORT` : will default to 5000 if not passed in run argument

```bash
docker run -d -e WEBEX_ACCESS_TOKEN={your bot token} ghcr.io/kourtneya/webex-webhook-test:latest
```
