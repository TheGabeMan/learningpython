import json
import time
import sec_read



with open('secret_strava_tokens.json') as importjson:
    strava_tokens = json.load(importjson)
    access_token = strava_tokens['access_token']
    refresh_token = strava_tokens['refresh_token']
    expire_token = strava_tokens['expires_at']

## If access tokne has expired then use the refresh token to get the new access token
if strava_tokens['expires_at'] < time.time():

    ## Make stava auth API call with current fresh token
     response = requests.post(
                        url = 'https://www.strava.com/oauth/token',
                        data = {
                                'client_id': [INSERT_CLIENT_ID_HERE],
                                'client_secret': '[INSERT_CLIENT_SECRET_KEY]',
                                'grant_type': 'refresh_token',
                                'refresh_token': strava_tokens['refresh_token']
                                }
                    )