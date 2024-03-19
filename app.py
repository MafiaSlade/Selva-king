from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# Load responses from JSON file
with open('responses.json') as f:
    responses = json.load(f)

# Function to get a random response
def get_response(intent):
    if intent in responses:
        return random.choice(responses[intent])
    else:
        return "Sorry, I don't understand that."

# Function to determine intent based on keywords
def get_intent(message):
    if any(word in message.lower() for word in ['hello', 'hi', 'hey']):
        return 'greetings'
    elif any(word in message.lower() for word in ['bye', 'goodbye']):
        return 'farewell'
    elif 'thank' in message.lower():
        return 'thanks'
    elif any(word in message.lower() for word in ['name', 'who']):
        return 'about'
    elif any(word in message.lower() for word in ['age', 'old']):
        return 'about'
    else:
        return 'fallback'


# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle chatbot requests
@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data['message']
    intent = get_intent(message)
    response = get_response(intent)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
