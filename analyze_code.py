# src/analyze_code.py

import requests
from config.config import ANTHROPIC_API_KEY

ANTHROPIC_HEADERS = {'x-api-key': ANTHROPIC_API_KEY, 'Content-Type': 'application/json'}

def analyze_with_anthropic(code):
    payload = {
        'model': 'claude-3-5-sonnet-20240620',
        'max_tokens': 1024,
        'messages': [{'role': 'user', 'content': f'Analyze this code: {code}'}]
    }
    response = requests.post('https://api.anthropic.com/v1/messages', headers=ANTHROPIC_HEADERS, json=payload)
    response.raise_for_status()
    return response.json()

def analyze_codebase(contents):
    results = []
    for file in contents:
        if file['type'] == 'file' and file['name'].endswith('.py'):
            content = requests.get(file['download_url']).text
            results.append({'file': file['name'], 'analysis': analyze_with_anthropic(content)})
    return results
