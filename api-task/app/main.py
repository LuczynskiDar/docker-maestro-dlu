import os, sys
from fastapi import FastAPI
from dotenv import load_dotenv

# load_dotenv()

ENVIRONMENT = os.getenv('ENVIRONMENT','dev')
VERSION = os.getenv('VERSION', '0.0.0')

app =  FastAPI()


@app.get('/health')
def health_check():
    return {
        'status': 'ok',
        'name': 'api-task',
        'version': VERSION,
        'env': ENVIRONMENT,
    }