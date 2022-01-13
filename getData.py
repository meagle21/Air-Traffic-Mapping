
import requests
import json
import time

class getData:

    def __init__(self):
        self.url = "https://opensky-network.org/api/states/all?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226"
        self.flightList = ""

    def get_url(self):
        """Method returns the url for the api request."""
        return self.url

    def set_flight_list(self):
        """Method gets the response to be parsed."""
        url = self.get_url() #get the url 
        res = requests.get(url) #get the web response
        flightList = res.json()['states'] #convert it to json and index into the states 
        self.flightList = flightList #set the flight list variable

    def get_flight_list(self):
        """Method returns the flight list."""
        return self.flightList
        
    def time_interval(self):
        """Method sleeps for the selcted time interval."""
        oneSecond = 1
        tenSeconds = 10
        time.sleep(tenSeconds)