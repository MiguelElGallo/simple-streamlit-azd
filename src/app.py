from flask import Flask, make_response
import sys

app = Flask(__name__)

@app.route('/')
def index():
    version = sys.version_info
    response = make_response(f"Hello World, I am Python {version.major}.{version.minor}", 200)
    response.mimetype = "text/plain"
    return response

if __name__ == '__main__':
    app.run(debug=True)
