# ============================================
#  AMON DOCKER - Production Flask Application
#  Author: fvjy12
# ============================================

import os
import time
import platform
import socket
from datetime import datetime

from flask import Flask, jsonify, request

app = Flask(__name__)

# Application metadata
APP_NAME = "AMON Docker"
APP_VERSION = "1.0.0"
START_TIME = time.time()


@app.route("/")
def home():
    """Main endpoint with app info"""
    return jsonify({
        "app": APP_NAME,
        "version": APP_VERSION,
        "author": "fvjy12",
        "status": "running",
        "message": "Welcome to AMON Docker!",
        "endpoints": [
            "/",
            "/health",
            "/info",
            "/time",
            "/echo"
        ]
    })


@app.route("/health")
def health():
    """Health check endpoint for Docker HEALTHCHECK"""
    return jsonify({
        "status": "healthy",
        "uptime_seconds": round(time.time() - START_TIME, 2)
    })


@app.route("/info")
def info():
    """System information endpoint"""
    return jsonify({
        "app": APP_NAME,
        "version": APP_VERSION,
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "container": os.environ.get("HOSTNAME", "unknown"),
        "environment": os.environ.get("APP_ENV", "production")
    })


@app.route("/time")
def current_time():
    """Current server time"""
    return jsonify({
        "time": datetime.now().isoformat(),
        "timezone": time.tzname
    })


@app.route("/echo", methods=["POST"])
def echo():
    """Echo endpoint - returns what you send"""
    data = request.get_json(silent=True) or {}
    return jsonify({
        "received": data,
        "method": request.method,
        "headers": dict(request.headers)
    })


if __name__ == "__main__":
    # For local development
    app.run(host="0.0.0.0", port=8080, debug=True)
