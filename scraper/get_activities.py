import stravatoken
import requests

url = "https://www.strava.com/api/v3/activities" + "?access_token=" + stravatoken.strava_tokens['access_token']

# Get first 20 activiteis from Strava
readStrava = requests.get(url)
readStrava = readStrava.json()

print( readStrava)
