from flask import Flask, render_template, request
from predict_iris import predict_iris
from flask import jsonify
app = Flask(__name__)


@app.route('/api', methods=['POST'])
def apiGet():
    payload = request.json
    sepal_length = float(payload['sepal_length'])
    sepal_width = float(payload['sepal_width'])
    petal_length = float(payload['petal_length'])
    petal_width = float(payload['petal_width'])
    features = [sepal_length, sepal_width, petal_length, petal_width]
    prediction = predict_iris(features)
    return jsonify({'iris_type': prediction})


@app.route('/api/<sepal_length>/<sepal_width>/<petal_length>/<petal_width>', methods=['GET'])
def apiPost(sepal_length, sepal_width, petal_length, petal_width):
    features = [float(sepal_length), float(sepal_width),
                float(petal_length), float(petal_width)]
    prediction = predict_iris(features)
    return jsonify({'iris_type': prediction})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)


