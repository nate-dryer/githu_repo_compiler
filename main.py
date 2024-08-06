# main.py

from src.fetch_repo import fetch_repo_contents
from src.analyze_code import analyze_codebase
from src.save_results import save_results

def main(owner, repo, output_format, output_folder):
    contents = fetch_repo_contents(owner, repo)
    results = analyze_codebase(contents)
    save_results(results, output_format, output_folder)

if __name__ == "__main__":
    owner = 'your_github_username'
    repo = 'your_repository_name'
    output_format = 'pdf'
    output_folder = './output'
    
    main(owner, repo, output_format, output_folder)
