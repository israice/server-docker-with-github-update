import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/webhook", methods=["POST"])
def webhook():
    if request.headers.get("X-GitHub-Event") == "push":
        # Fetch latest and reset to match remote exactly
        subprocess.run(["git", "fetch", "origin"], cwd="/app")
        subprocess.run(["git", "reset", "--hard", "origin/main"], cwd="/app")
        return "Updated", 200
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
