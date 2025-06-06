# Weather Summary Application

A FastAPI application that provides weather information and AI-generated weather summaries using WeatherAPI and Google's Gemini AI.

## Features

- Get current weather data for any location
- Generate AI-powered weather summaries with clothing recommendations
- Get custom responses from Gemini AI

## Prerequisites

- Python 3.8+
- FastAPI
- Pydantic
- python-dotenv
- requests

## Installation

1. Clone the repository:

2. Install the required dependencies:
```bash
pip install fastapi uvicorn dotenv requests 
```

3. Create a `.env` file in the root directory and add your API keys:
```
gemini=your_gemini_api_key_here
weather=your_weatherapi_key_here
```

**Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

## API Keys Setup

You'll need to obtain API keys from:
- [WeatherAPI](https://www.weatherapi.com/) - Sign up for a free API key
- [Google Gemini AI](https://makersuite.google.com/app/apikey) - Get your API key

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```

2. Access the Swagger UI documentation at:
```
http://localhost:8000/docs
```

## API Endpoints

### 1. GET /
- Basic hello world endpoint

### 2. POST /weather
- Get current weather data for a location
- Request body: `{"q": "city_name"}`

### 3. POST /summary
- Get AI-generated weather summary with recommendations
- Request body: `{"q": "city_name"}`

### 4. POST /ask
- Direct interaction with Gemini AI
- Request body format:
```json
{
    "contents": [
        {
            "parts": [
                {
                    "text": "your question here"
                }
            ]
        }
    ]
}
```

## Using Swagger UI

1. Open `http://localhost:8000/docs` in your browser
2. Click on any endpoint to expand it
3. Click "Try it out"
4. Enter the required parameters in the request body
5. Click "Execute" to see the response

## Security Notes

- Keep your API keys confidential
- Don't share your `.env` file
- Add `.env` to your `.gitignore` file
