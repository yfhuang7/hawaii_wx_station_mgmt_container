#/bin/python3
import json

token_file = json.load("tokens.json")

access_token = token_file['access_token']

print(access_token)
