from flask import Flask, render_template, request, jsonify
import random
import json
import numpy as np
import nltk
import pickle
import os
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

# Initialize Flask app
app = Flask(__name__)

# Global variables for loaded resources
lemmatizer = None
intents = None
words = None
classes = None
model = None

def load_resources():
    """Load all resources once when the function is first called"""
    global lemmatizer, intents, words, classes, model
    
    if lemmatizer is None:
        # Download NLTK resources if not already downloaded
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt', quiet=True)
        
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet', quiet=True)
        
        lemmatizer = WordNetLemmatizer()
    
    if intents is None:
        intents = json.load(open('intents.json'))
    
    if words is None:
        words = pickle.load(open('words.pkl', 'rb'))
    
    if classes is None:
        classes = pickle.load(open('classes.pkl', 'rb'))
    
    if model is None:
        model = load_model('vivek_customer_service_chatbot.h5')

# Preprocess user input
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)

    return_list = []
    for r in results:
        return_list.append({'intents': classes[r[0]], 'probability': str(r[1])})

    if not return_list:
        return_list.append({'intents': 'no_match', 'probability': '0'})

    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intents']
    for intent in intents_json['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "Sorry, I didn't understand that. Could you please rephrase?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=['POST'])
def chat():
    # Load resources on first request
    load_resources()
    
    user_msg = request.json.get("message")
    intents_list = predict_class(user_msg)
    response = get_response(intents_list, intents)
    return jsonify({"response": response})

# For local development
if __name__ == "__main__":
    app.run(debug=True)
