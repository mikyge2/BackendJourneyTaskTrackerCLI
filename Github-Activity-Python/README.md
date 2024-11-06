# GitHub User Activity Fetcher

This Python script fetches recent activities of a GitHub user using the GitHub Events API. It displays push events, issues opened, and starred repositories.

## Features
- Fetches recent public events for a given GitHub username.
- Displays:
  - Commits pushed to repositories.
  - Issues opened in repositories.
  - Repositories starred by the user.

## Requirements
- Python 3.x
- `requests` library (`pip install requests`)

## Usage
```bash
./fetch_user_activity.py <github_username>
