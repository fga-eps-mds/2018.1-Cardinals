from github_api.update_repository import get_github_repository
import re

def get_repository(address):
    regex = r'^(http|https)://(?P<git_domain>\w+).com/(?P<repository>.*)$'
    address_dict = re.match(regex, address).groupdict()
    domain = address_dict['git_domain']
    name_repository = address_dict['repository']

    repo = None

    if address_dict['git_domain'] == 'github':
        repo = get_github_repository(name_repository)
    
    return repo