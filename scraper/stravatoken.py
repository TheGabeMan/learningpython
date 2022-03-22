import json
import time
import requests
import globals

## Reading Client_ID and Client_Secret
globals.read_client()

## Open token file 
with open('secret_strava_tokens.json') as importjson:
    global strava_tokens
    strava_tokens = json.load(importjson)

## If access tokne has expired then use the refresh token to get the new access token
if strava_tokens['expires_at'] < time.time():

    ## Make stava auth API call with current fresh token
    print( 'Token expired, going to refresh the existing token')
    response = requests.post(
                        url = 'https://www.strava.com/oauth/token',
                        data = {
                                'client_id': globals.client_id,
                                'client_secret': globals.client_secret,
                                'grant_type': 'refresh_token',
                                'refresh_token': strava_tokens['refresh_token']
                                }
                            )
    strava_tokens = response.json()
    with open('secret_strava_tokens.json', 'w') as outfile:
        json.dump(strava_tokens, outfile)

print('Access Token: ', strava_tokens['access_token'])

