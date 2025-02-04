import os
import subprocess
#import yaml

def execute_command(command):
    """Execute a shell command and return its output or error."""
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def load_config(config_path="config.yaml"):
    """Load repository details from YAML configuration file."""
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        return config.get("repository", {})
    else:
        # Hardcoded fallback if config.yaml is not found
        return {
            "url": "https://github.com/Ultrapronandha/Demo.git",
            "branch": "main",
        }

def main():
    # Load configuration
    repo_details = load_config()

    # Extract repository details
    repo_url = repo_details.get("url")
    branch_name = repo_details.get("branch", "main")

    # Initialize Git repository if not already initialized
    if not os.path.exists(".git"):
        execute_command("git init")

    # Add files to staging
    execute_command("git add .")

    # Commit changes
    execute_command('git commit -m "Initial commit"')

    # Add remote origin
    execute_command(f"git remote add origin {repo_url}")

    # Set branch name
    execute_command(f"git branch -M {branch_name}")

    # Push to GitHub
    execute_command(f"git push -u origin {branch_name}")

if __name__ == "__main__":
    main()
