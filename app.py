from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def hello():
    return jsonify({"status": "ok", "message": "Hello from Flask on Render!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
