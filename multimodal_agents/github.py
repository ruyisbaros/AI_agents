import os
import requests
from dotenv import load_dotenv

from langchain_core.documents import Document

owner = "techwithtim"
repo = "Flask-Web-App-Tutorial"
endpoint = "issues"

# Load environment variables from .env file
load_dotenv("../.env")

github_token = os.getenv("GITHUB_TOKEN")


def fetch_github(owner, repo, endpoint):
    url = f"https://api.github.com/repos/{owner}/{repo}/{endpoint}"
    headers = {"Authorization": f"Bearer {github_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Failed to fetch data from GitHub: {response.status_code}")
        return []

    print(data[0])
    return data


def load_issues(issues):
    documents = []
    for issue in issues:
        metadata = {
            "body": issue["body"],
            "author": issue["user"]["login"],
            "labels": issue["labels"],
            "comments": issue["comments"],
            "created_at": issue["created_at"],
        }
        data = issue["title"]

        if issue["body"]:
            data += issue["body"]
        doc = Document(page_content=data, metadata=metadata)
        documents.append(doc)
    return documents


def fetch_github_issues(owner, repo):
    issues_data = fetch_github(owner, repo, endpoint="issues")
    return load_issues(issues_data)
