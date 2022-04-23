#!/bin/python3
from get_new_tokens import get_new_tokens
from encrypt_token import encrypt_token
from update_secret_rest_call import put_secret
import os

tokens: dict = get_new_tokens(
    ike_url=os.environ['ike_url'],
    ike_key=os.environ['ike_key'],
    ike_secret=os.environ['ike_secret'],
    ike_refresh=os.environ['ike_refresh']
)

# to be continued...