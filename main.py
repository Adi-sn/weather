from fastapi import FastAPI
import os, schemas 
from dotenv import load_dotenv
import requests
import services
load_dotenv()


app= FastAPI()

@app.get('/')
def intro():
    return {'message': 'Hello, World!'}

@app.post('/ask')
def ask(body: schemas.Content):
    return services.gemini(body=body)

@app.post('/weather')
def weather(body: schemas.Weather):
    return services.weather(body=body)

@app.post('/summary')
def summary(body: schemas.Weather):
    details=services.weather(body=body)

    #datils
    place=details['location']['name']
    temp = details["current"]["temp_c"]
    if details["current"]["is_day"] == 1:
        time = "Day"
    else:
        time = "Night"
    condition = details["current"]["condition"]["text"]
    wind = details["current"]["wind_kph"]
    feelslike = details["current"]["feelslike_c"]
    uv =details["current"]["uv"]

    prompt = f'Based on this weather, please provide a concise summary,Tell me if I should carry an umbrella, Suggest appropriate clothing for going outdoors and give one or two other relevant pieces of advice (e.g., about sun protection if sunny, or driving conditions if stormy), The location is {place}, temprature in celcius is {temp} but it feels like {feelslike}, it is currently {time}time and the weather is {condition} with a uv index of {uv}, the wind speeds in kmph are {wind}.'
    
    body = schemas.Content(
        contents=[
            schemas.Parts(
                parts=[
                    schemas.Text(text=prompt)
                ]
            )
        ]
    )
    return services.gemini(body=body)



