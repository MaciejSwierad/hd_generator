class FlightTicket:
    def __init__(self, id_db, place_number,
                 row_number, ticket_id, airlines, flight_id):
        self.db_id = id_db
        self.place_number = place_number
        self.row_number = row_number
        self.ticket_id = ticket_id
        self.airlines = airlines
        self.flight_id = flight_id

    def __str__(self) -> str:
        return f"{self.db_id} {self.place_number} {self.row_number} " \
               f"{self.ticket_id} {self.airlines} {self.flight_id} "
