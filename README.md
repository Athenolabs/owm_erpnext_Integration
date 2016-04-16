## Openweather Integration

This project is made to allow the easy connection between OWM and ERPNext. 

Settings Page:

Snapshot Tool:
Take a "snapshot" of weather using the automated API from OpenWeatherMap.org, and save it to the "Weather Logs" Document.

Weather Logs:
List of all informtation collected in read-only form for past API calls. Uses DATETIME of API call as the name of the document. 

## NOTE FROM AUTHOR

The real functionality of this code is to help me learn about ERPNext and how custom apps interact with the framework. 
The  code's purpose is to make an API call and return results from OWM's API. 

I am using the PyOWM Import to access the OWM Api and using this app to pass 
the API key and location data. 

I will be using this Integration to get and log weather data for the farm
and eventually perform automated actions based upon the weather

## EXAMPLE OF FUTURE USES:
    If it is currently raining, create task to check locations.
    If wind exceeds MPH set, BATTON DOWN THE HATCHES
    Turn lights on after sunset until set light requirement is met. 
    ETC.

