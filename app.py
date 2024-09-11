from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Customize CORS settings
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Endpoint to handle POST requests
@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
    
    # Process the received data (for example, save it to a file or database)
    print(data)  # Here, you can do anything with the data like saving it
    
    return jsonify({'message': 'Data received successfully'}), 200

# Home page
@app.route('/')
def home():
    return "Welcome to the Flask API!"

if __name__ == '__main__':
    app.run(debug=True)
