import pickle
import numpy as np
from flask import Flask
from flask import request
from flask import jsonify


def load(filename: str):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


# dv = load('dv.bin')
model = load('model.bin')

app = Flask('breast-cancer-diagnostic')


@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    # X = dv.transform([client])
    X = client
    client_data = list(client.values())
    X = np.array(client_data, dtype=np.float64).reshape((1, -1))
    y_pred = model.predict_proba(X)[0, 1]
    malignant = y_pred >= 0.5

    result = {
        'malignant_probability': float(malignant),
        'malignant': bool(malignant)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
