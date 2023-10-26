import requests
from flight_data import FlightData

API_URL = "https://api.tequila.kiwi.com/"
API_KEY = "YOUR TEQUILA API KEY"

class FlightSearch:

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


    def search_flight(self, departure_city_code, destination_city_code, date_from, date_to, max_stopovers=0):

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
            "max_stopovers": max_stopovers,
            "curr": "GBP",
        }

        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", params=query, headers=headers)
        print(response.text)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print("Trying with more stopovers")
            max_stopovers = 2
            query = {
                "fly_from": departure_city_code,
                "fly_to": destination_city_code,
                "date_from": date_from,
                "date_to": date_to,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "one_for_city": 1,
                "max_stopovers": max_stopovers,
                "curr": "GBP",
            }
            response = requests.get(url="https://api.tequila.kiwi.com/v2/search", params=query, headers=headers)
            print(response.text)
            try:
                data = response.json()["data"][0]
            except IndexError:
                print("No flight")
                return None

            flight_data = FlightData(departure_city=data["cityFrom"],
                                     destination_city=data["cityTo"],
                                     departure_airport=data["flyFrom"],
                                     destination_airport=data["flyTo"],
                                     via_city=data["route"][1]["cityFrom"],
                                     max_stopovers=2,
                                     price=data["price"],
                                     flight_date=data["route"][0]["local_departure"].split("T")[0],
                                     return_date=data["route"][2]["local_departure"].split("T")[0]
                                     )

            return flight_data

        flight_data = FlightData(departure_city=data["cityFrom"],
                                 destination_city=data["cityTo"],
                                 departure_airport=data["flyFrom"],
                                 destination_airport=data["flyTo"],
                                 price=data["price"],
                                 flight_date=data["route"][0]["local_departure"].split("T")[0],
                                 return_date=data["route"][1]["local_departure"].split("T")[0]
                                 )

        return flight_data



