import os
import subprocess
import numpy
def clone_or_pull_repo(repo_url, local_path):
    if not os.path.exists(local_path):
        print("Cloning the repository...")
        subprocess.run(["git", "clone", repo_url, local_path])
    else:
        print("Pulling the latest changes...")
        subprocess.run(["git", "-C", local_path, "pull"])

def create_workflow_file(local_repo_path, workflow_name, content):
    workflow_dir = os.path.join(local_repo_path, ".github", "workflows")
    os.makedirs(workflow_dir, exist_ok=True)

    workflow_path = os.path.join(workflow_dir, workflow_name)
    with open(workflow_path, "w") as file:
        file.write(content)
    
    print(f"Workflow file created/updated at {workflow_path}")

def commit_and_push_changes(local_repo_path, commit_message):
    subprocess.run(["git", "-C", local_repo_path, "add", "."])
    subprocess.run(["git", "-C", local_repo_path, "commit", "-m", commit_message], check=False)
    subprocess.run(["git", "-C", local_repo_path, "push"])

def main():
    repo_url = "https://github.com/Ultrapronandha/sample-repo.git"  # Update with the repository URL
    local_path = os.path.expanduser("~/Desktop/sample-repo")       # Local clone directory
    workflow_name = "python-app.yml"
    workflow_content = """
name: Python application

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.8'

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run tests
      run: pytest
"""

    clone_or_pull_repo(repo_url, local_path)
    create_workflow_file(local_path, workflow_name, workflow_content)
    commit_and_push_changes(local_path, "Update GitHub Actions workflow")

if __name__ == "__main__":
    main()
