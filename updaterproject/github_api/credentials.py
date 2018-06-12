import os

def get_credentials():
    ENV_USERNAME, ENV_PASSWORD = 'USERNAME', 'PASSWORD'
    env_credentials = [ENV_USERNAME, ENV_PASSWORD]
    credentials = map(os.environ.get, env_credentials)
    return tuple(credentials)
