from typing import List
from datetime import datetime, timedelta
import stravatoken
import requests
import time


## URL to retrieve the first "page" of activities
## url = "https://www.strava.com/api/v3/activities" + "?access_token=" + stravatoken.strava_tokens['access_token']
## URL to retrieve one specific strava activity, in this example 6865796332 is the activity ID:
## url = "https://www.strava.com/api/v3/activities/6865796332" + "?access_token=" + stravatoken.strava_tokens['access_token']

## To get past 50 days of activities calculate 'after' date in epochtime. 1 day = 86400 sec => 50 days = 4320000
daysHistory = 50
epochHistory = round(time.time() - (daysHistory * 86400))

## Since we need to know of each day if it was a rest day, and therefore no strava activity, we'll cycle through all days between today and epochHistory (start date)
## Startdate is formatted from epoch to datetime.date
startDate = datetime.date( datetime.fromtimestamp( epochHistory ))
print( "Start date = ", startDate)

## Url to get 60 activities per page and from 1644105600 = 6 feb 2022 12:00am GMT 
url = "https://www.strava.com/api/v3/athlete/activities?after=" + str( epochHistory ) + "&per_page=60" + "&access_token=" + stravatoken.strava_tokens['access_token']

# Get last activiteis from Strava
readStrava = requests.get(url)
ListOfActivities = readStrava.json()
print('Number of activities read: ', len(ListOfActivities))



## https://www.pressthered.com/adding_dates_and_times_in_python/
## convtime + timedelta(days=1)

EvalDate = startDate
Today = datetime.date( datetime.fromtimestamp( time.time() ))
while EvalDate <= Today:
    # print( "Eval day is: ", EvalDate, " ---  Today: ", Today)
    activityFound = False

    ## Now check to see if there is an activity on EvalDay
    ## Very dirty loop through all activities instead of searching through the activities
    for activity in ListOfActivities:
        StravaDate = datetime.date( datetime.strptime(activity["start_date_local"], "%Y-%m-%dT%H:%M:%SZ") )
        if EvalDate == StravaDate:
            print( "Strava date: ", StravaDate)
            activityFound = True

    if activityFound:
        print("For Evalday ", EvalDate, " one or more activities were found")

    EvalDate += timedelta(days=1)   ## Add one day to EvalDate










# for activity in ListOfActivities:
#    if activity["device_watts"]:
#        print( activity["id"], 
#            activity["name"],
#            activity["start_date_local"],
#            activity["trainer"],
#            activity["kilojoules"],
#            activity["workout_type"],
#            activity["device_watts"],
#            activity["weighted_average_watts"], 
#            activity["suffer_score"]
#            )
        
 #   else:
 #       print( activity["id"], 
 #           activity["name"],
 #           activity["start_date_local"],
 #           activity["trainer"],
 #           activity["kilojoules"],
 #           activity["workout_type"],
 #           activity["device_watts"]
 #           )

