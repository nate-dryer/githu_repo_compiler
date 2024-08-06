# src/fetch_repo.py

import requests
from config.config import GITHUB_TOKEN

GITHUB_HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}

def fetch_repo_contents(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}/contents'
    response = requests.get(url, headers=GITHUB_HEADERS)
    response.raise_for_status()
    return response.json()
