import webbrowser
import json
import requests


client_id = input('Your client ID: ')
client_secret = input('Your Client Secret: ')

## Wegschrijven client ID en Secret
with open('secret_client_id', 'w') as outfile:
    outfile.write( client_id ) 
    outfile.close

## Wegschrijven client ID en Secret
with open('secret_client_secret', 'w') as outfile:
    outfile.write( client_secret)
    outfile.close

### URL handmatig uitvoeren en dan de code plakken die terugkomt:
strava_url = "http://www.strava.com/oauth/authorize?client_id=" + client_id + "&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all"

webbrowser.open(strava_url,new=2)

### http://www.strava.com/oauth/authorize?client_id=32496&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all
## code = 'c5667666890bc9b64c9ae154a4ce4e35ab264cc6'
code = input("Copy the code from the URL: ")

# Make Strava auth API call with your 
# client_code, client_secret and code
response = requests.post(
                    url = 'https://www.strava.com/oauth/token',
                    data = {
                            'client_id': client_id,
                            'client_secret': client_secret,
                            'code': code,
                            'grant_type': 'authorization_code'
                            }
                )

#Save json response as a variable
strava_tokens = response.json()
print(strava_tokens)

# Save tokens to file
with open('secret_strava_tokens.json', 'w') as outfile:
    json.dump(strava_tokens, outfile)
