from os import read
from typing import List
from datetime import datetime, timedelta
import stravatoken
import requests
import time
import json


## URL to retrieve the first "page" of activities
## url = "https://www.strava.com/api/v3/activities" + "?access_token=" + stravatoken.strava_tokens['access_token']
## URL to retrieve one specific strava activity, in this example 6865796332 is the activity ID:
## url = "https://www.strava.com/api/v3/activities/6865796332" + "?access_token=" + stravatoken.strava_tokens['access_token']

## To get past 50 days of activities calculate 'after' date in epochtime. 1 day = 86400 sec => 50 days = 4320000
daysHistory = 50
epochHistory = round(time.time() - (daysHistory * 86400))

## Since we need to know of each day if it was a rest day, and therefore no strava activity, we'll cycle through all days between epochHistory (start date) and today
## Startdate is formatted from epoch to datetime.date
startDate = datetime.date( datetime.fromtimestamp( epochHistory ))
print( "Start date = ", startDate)

## Url to get 60 activities per page and from 1644105600 = 6 feb 2022 12:00am GMT 
url = "https://www.strava.com/api/v3/athlete/activities?after=" + str( epochHistory ) + "&per_page=60" + "&access_token=" + stravatoken.strava_tokens['access_token']

# Get last activities from Strava
readStrava = requests.get(url)
ListOfActivities = readStrava.json()
print('Number of activities read: ', len(ListOfActivities))


## Read the stored activities
try:
    readfile = open("activities.json", "r")
    storedDates = json.load(readfile)
except IOError:
    ## If the file doesn't exist, create json object in 'data'
    ## Since Fitness is calculated from the last 42 day average, only need to go back 42 days
    CheckDate = round(time.time() - (42 * 86400))
    print( "Checkdate :" , datetime.date( datetime.fromtimestamp( CheckDate )))
    print( "Isoformat: ", datetime.date( datetime.fromtimestamp( CheckDate )).isoformat() )

    storedFitness = {
         "dailyfitness" :
        [
            {
                "fitnessdate" : datetime.date( datetime.fromtimestamp( CheckDate )).isoformat(),
                "activityid" : 0,
                "name" : "dummy",
                "HRSS" : 0,
                "PSS" : 0,
                "Final Stress" : 0,
                "fitness" : 0,
                "fatigue" : 0,
                "form" : 0 
            }
       ]
    }

print( type(ListOfActivities))
def search_activity_on_date( name ):
    for keyval in ListOfActivities:
        if name.lower() == keyval['name'].lower():
            return keyval['start_date_local'], keyval['id']


## For every record in dailyfitness check if this date has any recordings in the strava file.
## In strava there can be mulitple recordings for one day
for fitnessday in storedFitness["dailyfitness"]:
    print( fitnessday["fitnessdate"])

    ## Check if Strava has an activity for that day, unfortunately by looping through
    searchfor = "Morning Ride"
    if (search_activity_on_date(searchfor) != None):
        print( "Found: ", search_activity_on_date(searchfor))

    else:
        print( searchfor, " is not found.") 


