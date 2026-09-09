import requests
import json


def github_profile(username):
    base_url = "https://api.github.com"

    # Get user information
    user_response = requests.get(
        f"{base_url}/users/{username}",
        timeout=10
    )

    # Get repository information
    repos_response = requests.get(
        f"{base_url}/users/{username}/repos",
        timeout=10
    )

    if user_response.status_code != 200:
        print("Error: GitHub user not found.")
        return

    if repos_response.status_code != 200:
        print("Error: Could not retrieve repositories.")
        return

    user = user_response.json()
    repos = repos_response.json()

    # Count programming languages
    languages = {}

    for repo in repos[:10]:
        language = repo.get("language")

        if language:
            languages[language] = languages.get(language, 0) + 1

    # Create profile
    profile = {
        "name": user.get("name"),
        "company": user.get("company"),
        "location": user.get("location"),
        "public_repos": user.get("public_repos"),
        "top_languages": languages,
        "bio": user.get("bio")
    }

    print("\n===== GITHUB PUBLIC PROFILE =====")
    print(json.dumps(profile, indent=2))


# Public GitHub lab account
github_profile("torvalds")