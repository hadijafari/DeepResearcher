from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Your app is running on Render."

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # This is where you handle the incoming request
    data = request.get_json()
    
    # Do something simple - log the request and return a response
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Received request at {current_time}")
    print(f"Request data: {data}")
    
    # Simple processing - you can modify this part
    response = {
        "status": "success",
        "message": "Request received and processed",
        "timestamp": current_time,
        "received_data": data
    }
    
    return jsonify(response)

@app.route('/test', methods=['GET'])
def test_endpoint():
    # Simple test endpoint you can call to verify the app works
    return jsonify({
        "status": "working",
        "message": "Test endpoint is responding",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
