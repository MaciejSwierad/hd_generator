class Baggage:
    def __init__(self, baggage_id, weight, type, ticket_id):
        self.db_id = baggage_id
        self.weight = weight
        self.type = type
        self.ticket_id = ticket_id

    def __str__(self) -> str:
        return f"{self.db_id} {self.weight} {self.type.name} {self.ticket_id}"
