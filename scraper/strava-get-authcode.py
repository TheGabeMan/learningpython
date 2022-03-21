import requests
import json

## Inlezen client_id
with open('secret_client_id') as importfile:
    client_id = importfile
    importfile.close

## Inlezen Secret
with open('secret_client_secret') as importfile:
    client_secret = importfile
    importfile.close

### URL handmatig uitvoeren en dan de code plakken die terugkomt:
### http://www.strava.com/oauth/authorize?client_id=32496&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all
code = 'c5667666890bc9b64c9ae154a4ce4e35ab264cc6'

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

## Wegschrijven client ID en Secret
with open('secret_client_id', 'w') as outfile:
    outfile.write( client_id)
    outfile.close

## Wegschrijven client ID en Secret
with open('secret_client_secret', 'w') as outfile:
    outfile.write( client_secret)
    outfile.close



# Open JSON file and print the file contents 
# to check it's worked properly
with open('strava_tokens.json') as check:
  data = json.load(check)

print(data)

