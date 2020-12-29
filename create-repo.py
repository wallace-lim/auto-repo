import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN_GITHUB")

def create(name):
    g = Github(token)
    g.get_user().create_repo(name)

if __name__ == "__main__":
    create(sys.argv[1].strip())

