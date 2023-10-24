#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
from notification_manager import NotificationManager

DEPARTURE_CITY = "YOUR DEPARTURE CITY"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_data()["prices"]

departure_city = DEPARTURE_CITY
departure_city_aita_code = flight_search.get_aita_code(departure_city)

date_today = datetime.now()
next_date = date_today + timedelta(days=180)

date_from = date_today.strftime("%d/%m/%Y")
date_to = next_date.strftime("%d/%m/%Y")


for city in sheet_data:
    destination_city_code = city["iataCode"]
    if destination_city_code == "":
        city["iataCode"] = flight_search.get_aita_code(city["city"])
        data_manager.update_data(city)
    flight = flight_search.search_flight(departure_city_aita_code, destination_city_code, date_from, date_to)
    flight_price = flight.price
    lowest_price = city["lowestPrice"]
    if flight_price < lowest_price:
        notification_manager.send_message(f"Low price alert! Only {flight.price} GBP to fly from "
                                          f"{flight.departure_city}-{flight.departure_airport} to "
                                          f"{flight.destination_city}-{flight.departure_airport}, "
                                          f"from {flight.flight_date} to {flight.return_date}")





