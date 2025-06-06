from fastapi import FastAPI
import os, schemas 
from dotenv import load_dotenv
import requests
load_dotenv()


app= FastAPI()

@app.get('/')
def intro():
    return {'message': 'Hello, World!'}

@app.post('/ask')
def ask(body : schemas.Content):
    api=os.getenv('gemini')
    response= requests.post(f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api}',json = body.model_dump())
    ans = response.json()
    return ans['candidates'][0]['content']['parts'][0]['text']
