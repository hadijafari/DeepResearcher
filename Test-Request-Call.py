from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Your app is running on Render."

def multiply_numbers(num1, num2):
    """Function to multiply two numbers"""
    return num1 * num2

def countdown_with_print(seconds):
    """Count down from given seconds, printing each second"""
    import time
    for i in range(seconds, 0, -1):
        print(f"Countdown: {i} seconds remaining...")
        time.sleep(1)
    print("Countdown finished!")

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

@app.route('/multiply', methods=['POST'])
def multiply_endpoint():
    """Endpoint to multiply two numbers with countdown"""
    try:
        data = request.get_json()
        
        # Get the two numbers from the request
        num1 = data.get('number1')
        num2 = data.get('number2')
        
        # Validate that both numbers are provided
        if num1 is None or num2 is None:
            return jsonify({
                "status": "error",
                "message": "Please provide both 'number1' and 'number2' in the request"
            }), 400
        
        # Convert to numbers (in case they're sent as strings)
        try:
            num1 = float(num1)
            num2 = float(num2)
        except (ValueError, TypeError):
            return jsonify({
                "status": "error",
                "message": "Both numbers must be valid numbers"
            }), 400
        
        print(f"Starting multiplication: {num1} × {num2}")
        
        # Perform the multiplication
        result = multiply_numbers(num1, num2)
        print(f"Calculation result: {result}")
        
        # Start the 20-second countdown
        print("Starting 20-second countdown...")
        countdown_with_print(20)
        
        # Prepare the response
        response = {
            "status": "success",
            "message": "Multiplication completed after countdown",
            "number1": num1,
            "number2": num2,
            "result": result,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        print(f"Sending response: {response}")
        return jsonify(response)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({
            "status": "error",
            "message": f"An error occurred: {str(e)}"
        }), 500

@app.route('/chatstate', methods=['POST'])
def process_chatstate():
    """Endpoint to process ChatState data"""
    try:
        data = request.get_json()
        
        print(f"Received ChatState data at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Parse and summarize the ChatState data
        summary = parse_chatstate_data(data)
        
        print("Parsed ChatState data successfully")
        print("Starting 20-second countdown...")
        
        # Start the 20-second countdown
        countdown_with_print(20)
        
        # Prepare the response
        response = {
            "status": "success",
            "message": "ChatState data processed successfully after countdown",
            "summary": summary,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        print(f"Sending ChatState response")
        return jsonify(response)
        
    except Exception as e:
        print(f"Error processing ChatState: {str(e)}")
        return jsonify({
            "status": "error",
            "message": f"An error occurred processing ChatState: {str(e)}"
        }), 500

def parse_chatstate_data(data):
    """Parse ChatState data and create a summary string"""
    try:
        business_name = data.get('business', {}).get('name', 'Unknown Business')
        stage = data.get('stage', 'Unknown Stage')
        language = data.get('language', 'Unknown Language')
        
        # Count competitors
        competitors_direct = len(data.get('competitors', {}).get('direct', []))
        
        # Create summary string
        summary = f"""
ChatState Analysis Summary:
==========================
Business: {business_name}
Stage: {stage}
Language: {language}
Direct Competitors: {competitors_direct}

Processing completed successfully!
        """.strip()
        
        return summary
        
    except Exception as e:
        return f"Error parsing ChatState data: {str(e)}"
        
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
