from os import read
from typing import List
from datetime import datetime, timedelta, date
import stravatoken
import requests
import time
import json


## URL to retrieve the first "page" of activities
## url = "https://www.strava.com/api/v3/activities" + "?access_token=" + stravatoken.strava_tokens['access_token']
## URL to retrieve one specific strava activity, in this example 6865796332 is the activity ID:
## url = "https://www.strava.com/api/v3/activities/6865796332" + "?access_token=" + stravatoken.strava_tokens['access_token']

## To get past 56 (8 weeks) days of activities calculate 'after' date in epochtime. 1 day = 86400 sec => 50 days = 4320000
daysHistory = 56
epochHistory = round(time.time() - (daysHistory * 86400))

## Since we need to know of each day if it was a rest day, and therefore no strava activity, we'll cycle through all days between epochHistory (start date) and today
## Startdate is formatted from epoch to datetime.date
startDate = datetime.date( datetime.fromtimestamp( epochHistory ))
print( "Start date = ", startDate)

## Url to get 112 activities per page and from 1644105600 = 6 feb 2022 12:00am GMT 
## 112 because potentially we could have 56 days of 2 activities per day, makes 112 activities. 
## Bigger numbers could also be true, but we'll see about that later.
url = "https://www.strava.com/api/v3/athlete/activities?after=" + str( epochHistory ) + "&per_page=112" + "&access_token=" + stravatoken.strava_tokens['access_token']

# Get last activities from Strava
readStrava = requests.get(url)
ListOfActivities = readStrava.json()
print('Number of activities read: ', len(ListOfActivities))

## Checking for every date between startDate and today

fitnessdate = startDate
while fitnessdate <= date.today():
    ## Check if fitnessday is found in ListOfActivities
    print( "Fitness date: ", fitnessdate)
    #StravaDate = datetime.date( datetime.strptime(activity["start_date_local"], "%Y-%m-%dT%H:%M:%SZ") )
    foundActivities = [x for x in ListOfActivities if datetime.date( datetime.strptime(x["start_date_local"], "%Y-%m-%dT%H:%M:%SZ") ) == fitnessdate ]
    # print( "FoundAct: ", type(foundActivities), len(foundActivities))
    if len(foundActivities) == 0:
        print( "        No activity today")

    else:
        for foundActivity in foundActivities:
            print( "        ", 
                foundActivity["id"], 
                foundActivity["name"],
                foundActivity["start_date_local"]
                )


    # End Loop of fitnessdate
    fitnessdate = fitnessdate + timedelta(days=1)
