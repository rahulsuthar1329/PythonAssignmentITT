import requests
from configure_credentials import credential
from data_processing import generate_random_id, extract_date, reverse_date


def get_response(url):
    headers = {"Authorization": f"Bearer {credential['GITHUB_TOKEN']}"}
    try:
        response = requests.get(url, headers=headers)
        json_data = response.json()
        return json_data
    except Exception as e:
        print('Error:', e)
        return None


def get_github_repos(users, limit=5):
    repos = []

    for user in users:
        for repo in get_response(user['repos_url'])[:5]:
            github_repo = {
                'github_username': user['github_username'],
                'github_email': user['email'],
                'repo_id': repo['id'],
                'repo_name': repo['name'],
                'is_repo_private': repo['private'],
                'repo_description': repo['description'],
                'repo_open_issues_count': repo['open_issues'],
                'repo_last_updated_date': reverse_date(extract_date(repo['updated_at']))
            }
            repos.append(github_repo)

    return repos


def get_github_users():
    users = []

    for user in get_response(f"{credential['BASE_URI']}/users"):
        user_data = get_response(user['url'])
        github_user = {
            'id': user_data['id'],
            'formatted_id': generate_random_id(user_data['id']),
            'github_username': user_data['login'],
            'github_profile_url': user_data['html_url'],
            'name': user_data['name'],
            'company_name': user_data['company'],
            'blog_url': user_data['blog'],
            'location': user_data['location'],
            'email': user_data['email'],
            'repos_url': user_data['repos_url'],
            'total_followers': user_data['followers'],
            'total_public_repos': user_data['public_repos'],
            'last_updated_date': extract_date(user_data['updated_at'])
        }
        users.append(github_user)

    return users
