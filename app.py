from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>My DevOps Deployment Pipeline</h1>
    <p>Flask application is running successfully!</p>
    <p>Built with Python, Docker and GitHub Actions.</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)