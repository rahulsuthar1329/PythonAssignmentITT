import json


def load_config(config_file='credentials.json'):
    with open(config_file) as f:
        return json.load(f)


credential = load_config()
