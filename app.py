from flask import Flask, jsonify
from datetime import datetime, timezone
import time

app = Flask(__name__)

START_TIME = time.monotonic()


@app.route("/")
def home():
    return jsonify({
        "application": "Homelab Status API",
	"version": "1.0.0",
	"message": "Welcome to my DevOps homelab!"
    })


@app.route("/health")
def health():
    return jsonify({
	"status": "healthy"
    })


@app.route("/api/status")
def status():
    return jsonify({
	"application": "Homelab Status API",
	"status": "running",
	"timestamp": datetime.now(timezone.utc).isoformat(),
	"uptime_seconds": round(time.monotonic() - START_TIME, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
