# Simple Flask API for Render

A lightweight Flask web application that can be deployed on Render to handle various API requests with processing delays and data analysis.

## What This App Does

This Flask application provides several endpoints that:
- Accept incoming HTTP requests
- Process data with customizable delays
- Return structured JSON responses
- Log activities for monitoring

### Available Endpoints

1. **Home Endpoint** (`/`) - Basic health check
2. **Test Endpoint** (`/test`) - Simple test endpoint
3. **Webhook Endpoint** (`/webhook`) - General purpose webhook handler
4. **Multiply Endpoint** (`/multiply`) - Performs multiplication with 20-second countdown
5. **ChatState Endpoint** (`/chatstate`) - Processes business analysis data with 20-second countdown

## Deployment on Render

### Prerequisites
- GitHub account
- Render account (free tier available)

### Files Required
- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies

### Deployment Steps
1. Create a GitHub repository with the project files
2. Connect repository to Render
3. Configure Render service:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Deploy and get your app URL (e.g., `https://your-app-name.onrender.com`)

## How to Use the API

### 1. Basic Health Check

Test if your app is running:

```bash
curl https://your-app-name.onrender.com
```

**Expected Response:**
```
Hello! Your app is running on Render.
```

### 2. Test Endpoint

Verify the app is working properly:

```bash
curl https://your-app-name.onrender.com/test
```

**Expected Response:**
```json
{
  "status": "working",
  "message": "Test endpoint is responding",
  "timestamp": "2025-06-06 10:30:45"
}
```

### 3. Simple Webhook

Send basic data to the webhook:

**PowerShell:**
```powershell
Invoke-RestMethod -Uri "https://your-app-name.onrender.com/webhook" -Method POST -ContentType "application/json" -Body '{"message": "Hello from external service"}'
```

**Curl:**
```bash
curl -X POST https://your-app-name.onrender.com/webhook -H "Content-Type: application/json" -d "{\"message\": \"Hello from external service\"}"
```

### 4. Multiplication with Countdown

Send two numbers to multiply with a 20-second processing delay:

**PowerShell:**
```powershell
Invoke-RestMethod -Uri "https://your-app-name.onrender.com/multiply" -Method POST -ContentType "application/json" -Body '{"number1": 15, "number2": 7}'
```

**Curl:**
```bash
curl -X POST https://your-app-name.onrender.com/multiply -H "Content-Type: application/json" -d "{\"number1\": 15, \"number2\": 7}"
```

**Expected Response (after 20 seconds):**
```json
{
  "status": "success",
  "message": "Multiplication completed after countdown",
  "number1": 15,
  "number2": 7,
  "result": 105,
  "timestamp": "2025-06-06 10:30:45"
}
```

### 5. ChatState Business Analysis

Send business data for analysis with a 20-second processing delay:

**PowerShell:**
```powershell
Invoke-RestMethod -Uri "https://your-app-name.onrender.com/chatstate" -Method POST -ContentType "application/json" -Body '{"stage":"complete","business":{"name":"FitAI Pro"},"language":"English","competitors":{"direct":["MyFitnessPal","Strava"]}}'
```

**Curl:**
```bash
curl -X POST https://your-app-name.onrender.com/chatstate -H "Content-Type: application/json" -d "{\"stage\":\"complete\",\"business\":{\"name\":\"FitAI Pro\"},\"language\":\"English\",\"competitors\":{\"direct\":[\"MyFitnessPal\",\"Strava\"]}}"
```

**Expected Response (after 20 seconds):**
```json
{
  "status": "success",
  "message": "ChatState data processed successfully after countdown",
  "summary": "ChatState Analysis Summary:\n==========================\nBusiness: FitAI Pro\nStage: complete\nLanguage: English\nDirect Competitors: 2\n\nProcessing completed successfully!",
  "timestamp": "2025-06-06 10:30:45"
}
```

## Command Line Usage Tips

### Using PowerShell (Recommended for Windows)
PowerShell's `Invoke-RestMethod` handles JSON better and provides cleaner output:

```powershell
Invoke-RestMethod -Uri "https://your-app-name.onrender.com/test"
```

### Using Curl
Available on most systems, but requires careful quote escaping:

```bash
curl -X POST https://your-app-name.onrender.com/endpoint -H "Content-Type: application/json" -d "{\"key\": \"value\"}"
```

### Monitoring Logs
- Go to your Render dashboard
- Click on your service
- View the "Logs" tab to see real-time processing and countdown output

## Response Times

- **Immediate responses:** `/`, `/test`, `/webhook`
- **20-second delay:** `/multiply`, `/chatstate`

During the 20-second delay, the server is actively counting down (visible in Render logs), and your terminal will wait for the response.

## Error Handling

Common errors and solutions:

| Error | Cause | Solution |
|-------|-------|----------|
| 404 Not Found | Endpoint doesn't exist | Check URL spelling and endpoint availability |
| 400 Bad Request | Invalid JSON format | Verify JSON syntax and required fields |
| 405 Method Not Allowed | Wrong HTTP method | Use POST for data submission, GET for simple requests |
| 500 Internal Server Error | Server processing error | Check Render logs for detailed error information |

## Example Use Cases

1. **Testing webhooks** from external services
2. **Simulating delayed processing** for testing async workflows
3. **Data validation** and analysis with structured responses
4. **Learning API development** and deployment workflows

## Local Development

To run locally for testing:

```bash
pip install -r requirements.txt
python app.py
```

Then test against `http://localhost:5000` instead of your Render URL.

## Notes

- Free Render apps sleep after 15 minutes of inactivity
- First request after sleeping may take 30+ seconds to wake up
- Processing delays are intentional for demonstration purposes
- All data is processed in memory and not stored permanently
