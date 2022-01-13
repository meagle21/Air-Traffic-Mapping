
from getData import *
from updateCSV import *

def main():
    csv = updateCSV()
    api = getData()

    while True:
        api.time_interval() #have while loop wait
        api.set_flight_list() #from the webpage get the flight list
        flights = api.get_flight_list() #get the flight list
        csv.read_in_data(flights)
        #csv.read_in_track_data(flights)



main()