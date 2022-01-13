
import csv
from datetime import *

class updateCSV:

    def __init__(self):
        self.fileName = "planePosition.csv"
    
    def read_in_data(self, flightData):
        """Reads in the data and imports it into the csv file."""
        fields = ["identity","lat","long","altitude","track"] #headers
        csvFile = open(self.fileName, 'w', newline='')
        csvwriter = csv.writer(csvFile)
        csvwriter.writerow(fields)
        for flight in flightData: #for flight in the flight data
            onGround = flight[8] #get the on ground flight boolean value
            if onGround: #if the flight is on the ground
                pass #ignore this value
            else: #if the flight is not on the ground
                #callSign = str(flight[1].strip()) #get the callsign value
                country = flight[2].strip() #get the origin country value
                #identity = str(str(callSign)+"."+str(country))
                latitude = flight[6] #get the latitude value
                longitude = flight[5] #get the longitude value
                alt = flight[13] #get the altitude value
                track = flight[10]  #get the track
                vals = [country, latitude, longitude, alt, track] #put all of these values into a list
                csvwriter.writerow(vals) #write these values to a row