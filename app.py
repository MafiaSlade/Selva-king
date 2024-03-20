from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load Thirukkural data from JSON file
with open('thirukkural.json', 'r', encoding='utf-8') as file:
    thirukkural_data = json.load(file)['kural']

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for fetching Thirukkural by number
@app.route('/get_kural', methods=['POST'])
def get_kural():
    number = int(request.form['number'])
    kural = next((k for k in thirukkural_data if k['number'] == number), None)
    if kural:
        return jsonify(kural)
    else:
        return jsonify({'error': 'Kural not found'})

if __name__ == '__main__':
    app.run(debug=True)
