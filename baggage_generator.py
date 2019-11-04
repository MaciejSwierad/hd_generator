import random

from baggage import Baggage


def generate_baggage(baggage_id, ticket_id, type):
    return Baggage(
        baggage_id,
        generate_weight(),
        type,
        ticket_id
    )


def generate_weight():
    return random.randint(10, 50)
