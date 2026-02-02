import hashlib
import hmac
import os
import subprocess

from flask import Flask, render_template, request

app = Flask(__name__)
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "")


def verify_signature(payload, signature):
    if not WEBHOOK_SECRET:
        return False
    expected = "sha256=" + hmac.new(
        WEBHOOK_SECRET.encode(), payload, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers.get("X-Hub-Signature-256", "")
    if not verify_signature(request.data, signature):
        return "Forbidden", 403

    if request.headers.get("X-GitHub-Event") == "push":
        subprocess.run(["git", "fetch", "origin"], cwd="/app")
        subprocess.run(["git", "reset", "--hard", "origin/main"], cwd="/app")
        return "Updated", 200
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
