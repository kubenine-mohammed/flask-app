from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status": "ok", "message": "Hello from EKS!"})

@app.route("/hello")
def hello():
    return jsonify({
        "status": "ok",
        "message": "Hello endpoint working!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

