class Ticket:
    def __init__(self, db_id, price, date_of_birth, date_of_flight, date_of_purchase,
                 document_id, ticket_id, flight_id, airplane_id, name,
                 surname, document_type, plec):
        self.db_id = db_id
        self.price = price
        self.date_of_birth = date_of_birth.strftime("%Y-%m-%d")
        self.date_of_flight = date_of_flight
        self.date_of_purchase = date_of_purchase
        self.document_id = document_id
        self.ticket_id = ticket_id
        self.flight_id = flight_id
        self.airplane_id = airplane_id
        self.name = name
        self.surname = surname
        self.document_type = document_type
        self.plec = plec

    def __str__(self) -> str:
        string_date_of_purchase = self.date_of_purchase.strftime("%Y-%m-%d")
        string_date_of_birth = self.date_of_birth.strftime("%Y-%m-%d")
        string_date_of_flight = self.date_of_flight[0].strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.db_id} {self.price} {string_date_of_birth} {string_date_of_flight} " \
               f"{string_date_of_purchase} {self.document_id} {self.ticket_id} {self.flight_id} " \
               f"{self.airplane_id} {self.name} {self.surname} {self.document_type} {self.plec}"
