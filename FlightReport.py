class FlightReport:
    def __init__(self, start_of_flight, landing_date, passengers_amount,
                 delay, airlines, airplane_id, flight_id):
        self.start_of_flight = start_of_flight
        self.landing_date = landing_date
        self.passengers_amount = passengers_amount
        self.delay = delay
        self.airlines = airlines
        self.airplane_id = airplane_id
        self.flight_id = flight_id

    def __str__(self) -> str:
        string_start_of_flight = ""
        try:
            string_start_of_flight = self.start_of_flight.strftime("%Y-%m-%d")
        except Exception:
            string_start_of_flight = self.start_of_flight[0].strftime("%Y-%m-%d")
        string_landing_date = self.landing_date.strftime("%Y-%m-%d")

        return f"{string_start_of_flight} {string_landing_date} {self.passengers_amount} " \
               f"{self.delay} {self.airlines} {self.airplane_id} {self.flight_id}"
