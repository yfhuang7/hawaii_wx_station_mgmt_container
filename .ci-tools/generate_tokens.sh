#!/bin/bash
curl -u $ike_key:$ike_secret \
          -d  grant_type=refresh_token \
          -d refresh_token=$ike_refresh \
          https://ikeauth.its.hawaii.edu/token > tokens.json
