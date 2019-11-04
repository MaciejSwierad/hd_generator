class FlightTicket:
    def __init__(self, flight_ticket_id, place_number,
                 row_number, ticket_id, airlines):
        self.db_id = flight_ticket_id
        self.place_number = place_number
        self.row_number = row_number
        self.ticket_id = ticket_id
        self.flight_ticket_id = flight_ticket_id
        self.airlines = airlines

    def __str__(self) -> str:
        return f"{self.db_id} {self.place_number} {self.row_number} " \
               f"{self.ticket_id} {self.flight_ticket_id} {self.airlines} "
