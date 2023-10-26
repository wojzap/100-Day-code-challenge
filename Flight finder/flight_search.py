import requests
from flight_data import FlightData

API_URL = "https://api.tequila.kiwi.com/"
API_KEY = "YOUR API KEY"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.aita_code = ""

    def get_aita_code(self, city):
        headers = {
            "apikey": API_KEY
        }
        response = requests.get(url=f"https://api.tequila.kiwi.com/locations/query?"
                                    f"term={city}&"
                                    f"locale=en-US&"
                                    f"location_types=city&"
                                    f"limit=1&active_only=true",
                                headers=headers)
        location_data = response.json()
        self.aita_code = location_data["locations"][0]["code"]
        return self.aita_code


    def search_flight(self, departure_city_code, destination_city_code, date_from, date_to):

        headers = {
            "apikey": API_KEY
        }

        query = {
            "fly_from": departure_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", params=query, headers=headers)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None

        flight_data = FlightData(departure_city=data["cityFrom"],
                                 destination_city=data["cityTo"],
                                 departure_airport=data["flyFrom"],
                                 destination_airport=data["flyTo"],
                                 price=data["price"],
                                 flight_date=data["route"][0]["local_departure"].split("T")[0],
                                 return_date=data["route"][1]["local_departure"].split("T")[0])

        return flight_data



