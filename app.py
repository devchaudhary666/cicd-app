from flask import Flask
import os
import socket

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "v2")

@app.route("/")
def home():
    pod = socket.gethostname()
    return f"""
    <h2>GitOps Forge — {VERSION}</h2>
    <p>Running on pod: <strong>{pod}</strong></p>
    <p>Deployed automatically via GitHub Actions + k3s</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
