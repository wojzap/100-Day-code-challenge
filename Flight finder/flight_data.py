class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, departure_city, departure_city_aita_code, destination_city,
                 destination_city_aita_code, price, flight_date, return_date):
        self.departure_city = departure_city
        self.departure_city_aita_code = departure_city_aita_code
        self.destination_city = destination_city
        self.destination_city_aita_code = destination_city_aita_code
        self.price = price
        self.flight_date = flight_date
        self.return_date = return_date
