import requests

def authenticate_with_github_api(token):
    headers = {'Authorization': f'token {token}'}

    response = requests.get('https://api.github.com/ra312', headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to authenticate with GitHub API')
        return None
