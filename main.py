import nltk
import numpy as np
import keras
import os

from flask import Flask, request, jsonify

script_dir = os.path.dirname(os.path.realpath(__file__))

nltk.download("wordnet")
wnl = nltk.WordNetLemmatizer()

packed_model = keras.models.load_model(f"{script_dir}/production.keras")
tokenizer = packed_model.layers[0]
label_lookup = packed_model.layers[1]
label_vocab = label_lookup.get_vocabulary()
model = packed_model.layers[2]


def lemmatize(sentence: str) -> str:
    sentence = sentence.lower().strip()
    words = [wnl.lemmatize(word) for word in sentence.split()]
    return " ".join(words)


app = Flask(__name__)


@app.post("/predict")
def predict():
    body = request.json
    tasks = body["tasks"]
    tasks = [lemmatize(x) for x in tasks]
    tasks_vec = tokenizer(tasks).numpy()
    predictions = model.predict(tasks_vec)
    labels = [str(label_vocab[np.argmax(x)]) for x in predictions]
    return jsonify({"labels": labels})


if __name__ == "__main__":
    app.run(port=8000)
