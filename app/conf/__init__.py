import json
import os

cwd = os.getcwd()
path = os.path.join(cwd,"app", "conf","headers.json")
with open(path) as config_file:
    data = json.load(config_file)
    username = data['headers']['username']
    password = data['headers']['password']
    security_token = data['headers']['security_token']

    content_type = data['tmo_headers']['Content-Type']
    token = data['tmo_headers']['Token']
    database = data['tmo_headers']['Database']
    user_agent = data['tmo_headers']['User-Agent']



    
