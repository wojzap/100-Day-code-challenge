import requests

SHEETY_API = "YOUR SHEETY API"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {}


    def get_data(self):
        response = requests.get(SHEETY_API)
        data = response.json()
        self.data = data
        return self.data

    def update_data(self, city_data):
        new_params = {
            "price": {
                "city": city_data["city"],
                "iataCode": city_data["iataCode"],
                "id": city_data["id"],
                "lowestPrice": city_data["lowestPrice"]
            }
           }
        response = requests.put(url=f"{SHEETY_API}/{city_data['id']}", json=new_params)
        print(response.text)
