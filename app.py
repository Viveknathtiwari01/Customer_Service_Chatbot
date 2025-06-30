from flask import Flask, render_template, request, jsonify
import random
import json
import re
import os

# Initialize Flask app
app = Flask(__name__)

# Global variables for loaded resources
intents = None

def load_resources():
    """Load all resources once when the function is first called"""
    global intents
    
    if intents is None:
        intents = json.load(open('intents.json'))

def clean_up_sentence(sentence):
    """Clean and tokenize the sentence"""
    sentence = sentence.lower()
    sentence = re.sub(r'[^\w\s]', '', sentence)
    return sentence.split()

def calculate_similarity(sentence1, sentence2):
    """Calculate simple word-based similarity"""
    words1 = set(clean_up_sentence(sentence1))
    words2 = set(clean_up_sentence(sentence2))
    
    if not words1 or not words2:
        return 0
    
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    
    return len(intersection) / len(union)

def predict_class(user_message):
    """Predict the intent using pattern matching"""
    best_match = None
    best_score = 0
    
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            score = calculate_similarity(user_message, pattern)
            if score > best_score:
                best_score = score
                best_match = intent['tag']
    
    # Return default if no good match found
    if best_score < 0.3:
        return [{'intents': 'no_match', 'probability': '0'}]
    
    return [{'intents': best_match, 'probability': str(best_score)}]

def get_response(intents_list, intents_json):
    """Get response based on predicted intent"""
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
