#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_data()["prices"]

departure_city = "London"
departure_city_aita_code = flight_search.get_aita_code(departure_city)

date_today = datetime.now()
next_date = date_today + timedelta(days=180)
date_from = date_today.strftime("%d/%m/%Y")
date_to = next_date.strftime("%d/%m/%Y")

#
# for city in sheet_data:
#     if city["iataCode"] == "":
#         city["iataCode"] = flight_search.get_aita_code(city["city"])
#         data_manager.update_data(city)


# TEST
flight = flight_search.search_flight(departure_city_aita_code, flight_search.get_aita_code("Krakow"), date_from, date_to)

print(flight.price)
print(flight.flight_date)
print(flight.return_date)
