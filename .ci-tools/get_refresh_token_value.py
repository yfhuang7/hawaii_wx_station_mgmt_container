#/bin/python3
import json

token_file = json.load("tokens.json")

refresh_token = token_file['refresh_token']

print(refresh_token)
