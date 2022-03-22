from typing import List
from datetime import datetime
import stravatoken
import requests

## URL to retrieve the first "page" of activities
url = "https://www.strava.com/api/v3/activities" + "?access_token=" + stravatoken.strava_tokens['access_token']
## URL to retrieve one specific strava activity, in this example 6865796332 is the activity ID:
## url = "https://www.strava.com/api/v3/activities/6865796332" + "?access_token=" + stravatoken.strava_tokens['access_token']


# Get first 20 activiteis from Strava
readStrava = requests.get(url)
ListOfActivities = readStrava.json()

for activity in ListOfActivities:
    if activity["device_watts"]:
        print( activity["id"], activity["name"],activity["start_date_local"],round(activity["distance"]/1000,2),activity["total_elevation_gain"],activity["trainer"],activity["average_speed"],activity["kilojoules"],activity["workout_type"],activity["device_watts"],activity["weighted_average_watts"], activity["suffer_score"])
        
    else:
        print( activity["id"], activity["name"],activity["start_date_local"],round(activity["distance"]/1000,2),activity["total_elevation_gain"],activity["trainer"],activity["average_speed"],activity["kilojoules"],activity["workout_type"],activity["device_watts"])

