from github_api import get_github_users, get_github_repos
from data_processing import (reverse_date,convert_to_dataframe,replace_empty_values,
                             sort_values,apply_function,dataframe_to_csv, drop_column)

users = get_github_users()
repos = get_github_repos(users)

users_dataframe = convert_to_dataframe(users)
users_dataframe = replace_empty_values(users_dataframe)
users_dataframe = sort_values(users_dataframe, 'last_updated_date')
users_dataframe['last_updated_date'] = apply_function(users_dataframe, 'last_updated_date', reverse_date)
users_dataframe = drop_column(users_dataframe, 'repos_url')
dataframe_to_csv(users_dataframe, 'github_users.csv')

repos_dataframe = convert_to_dataframe(repos)
repos_dataframe = replace_empty_values(repos_dataframe)
repos_dataframe = sort_values(repos_dataframe, 'repo_open_issues_count')
dataframe_to_csv(repos_dataframe, 'github_repos.csv')
