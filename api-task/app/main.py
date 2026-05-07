import os, sys
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

ENVIRONMENT = os.getenv('ENV','dev')

app =  FastAPI()

@app.get('/health')
def health_check():
    return {
        'status': 'ok',
        'name': 'api-task',
        'version': '1.0',
        'env': f"{ENVIRONMENT}",
    }