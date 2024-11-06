#!/usr/bin/env python3

import sys
import requests

def fetch_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        events = response.json()

        for event in events:
            event_type = event['type']
            repo_name = event['repo']['name']

            # Handle PushEvent
            if event_type == "PushEvent":
                commits = len(event['payload']['commits'])
                print(f"Pushed {commits} commit(s) to {repo_name}")

            # Handle IssuesEvent (for new issues opened)
            elif event_type == "IssuesEvent" and event['payload']['action'] == "opened":
                issue_title = event['payload']['issue']['title']
                print(f"Opened a new issue in {repo_name}: {issue_title}")

            # Handle WatchEvent (for starring a repository)
            elif event_type == "WatchEvent":
                print(f"Starred {repo_name}")

            # Add handling for other events if necessary
            else:
                print(f"{event_type} in {repo_name}")

    else:
        print(f"Failed to fetch data for user {username}, Status code: {response.status_code}")

def main():
    if len(sys.argv) > 1:
        # Get the arguments (excluding the script name)
        args = sys.argv[1]
        print("Github Username:", args)
        fetch_user_activity(args)
    else:
        print("No Username passed")
    
if __name__ == '__main__':
    main()
