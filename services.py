from dotenv import load_dotenv
import os
import requests
import schemas
load_dotenv()


def gemini(body : schemas.Content):
    api=os.getenv('gemini')
    response= requests.post(f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api}',json = body.model_dump())
    ans = response.json()
    return ans['candidates'][0]['content']['parts'][0]['text']

def weather(body : schemas.Weather):
    api=os.getenv('weather')
    response= requests.post(f'http://api.weatherapi.com/v1/current.json?key={api}&q={body.q}',json = body.model_dump())
    ans = response.json()
    return ans