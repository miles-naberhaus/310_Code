from flask import Flask, render_template, jsonify, request
from rand import Chief
from gpio import forward, backward, left, right, stop

app = Flask(__name__)


@app.route('/')
def index():
    # Create default webpage
    return render_template('index.html')


@app.route('/chief/', methods=['POST'])
def chief():
    # Upon POST to this route, call "chief" method
    key = request.values.get("key")
    if key == "c":
        Chief()
    return jsonify(request.values)

@app.route('/move/', methods=['POST'])
def move():
    # Take JSON from javascript POST, convert to functions in GPIO
    key = request.values.get("key")
    if key == "ArrowUp":
        forward()
    elif key == "ArrowDown":
        backward()
    elif key == "ArrowLeft":
        left()
    elif key == "ArrowRight":
        right()
    elif key == " ":
        stop()
    return jsonify(request.values)

@app.route('/stop/', methods=['POST'])
def st():
    # Call a single gpio "stop" function
    stop()
    return jsonify(request.values)

if __name__ == "__main__":
    app.run(debug=True)