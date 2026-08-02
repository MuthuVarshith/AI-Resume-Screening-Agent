from http import HTTPStatus
from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def home():
    return jsonify({
        "message": "AI Resume Screening Agent",
        "status": "ok"
    }), HTTPStatus.OK

if __name__ == '__main__':
    app.run(debug=True)
