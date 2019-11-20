from flight_ticket import FlightTicket

PLACE_NUMBERS = 25


# max amount

def generate_flight_ticket(global_flight_ticket_id, prev_sit, airlines, flight_id):
    sit = generate_sit(prev_sit)
    return FlightTicket(
        global_flight_ticket_id,
        sit[1],
        sit[0],
        None,
        airlines,
        flight_id
    )


# def generate_flight_ticket(flight_ticket_id, place_number, row_number, ticket_id, airlines):
#     return FlightTicket(flight_ticket_id, place_number, row_number, ticket_id, airlines)

def generate_sit(prev_sit):
    if prev_sit is None:
        return 1, 1
    return prev_sit[0] + (int)(prev_sit[1] / PLACE_NUMBERS), (prev_sit[1] % PLACE_NUMBERS) + 1
