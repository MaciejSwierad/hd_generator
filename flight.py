class Flight:
    def __init__(self, db_id, flight_start_date,
                 flight_end_date, flight_id, airplane_id,
                 airline, from_place, to_place):
        self.db_id = db_id
        self.flight_start_date = flight_start_date
        self.flight_end_date = flight_end_date
        self.flight_id = flight_id
        self.airplane_id = airplane_id
        self.airline = airline
        self.from_place = from_place
        self.to_place = to_place

    def __str__(self) -> str:
        string_flight_start_date = self.flight_start_date[0].strftime("%Y-%m-%d %H:%M:%S")
        string_flight_end_date = self.flight_end_date.strftime("%Y-%m-%d %H:%M:%S")

        return f"{self.db_id} {string_flight_start_date} {string_flight_end_date} " \
               f"{self.flight_id} {self.airplane_id} {self.airline} {self.from_place} " \
               f"{self.to_place}"
