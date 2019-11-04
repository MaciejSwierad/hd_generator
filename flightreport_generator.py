import datetime
import random

from FlightReport import FlightReport

DELAY_CHANCES_PERCENT = 10
HUGE_DELAY_CHANCES_IF_DELAY_HAPPENED_PERCENT = 5

DELAY_MIN_MINUTES = 1
DELAY_MAX_MINUTES = 30

HUGE_DELAY_MIN_MINUTES = 60
HUGE_DELAY_MAX_MINUTES = 240


def generate_flight_report(planned_start_of_flight, flight_length_minutes, passengers_amount,
                           airlines, airplane_id, flight_id):
    if random.randint(0, 100) > DELAY_CHANCES_PERCENT:
        return FlightReport(
            planned_start_of_flight,
            planned_start_of_flight[0] + datetime.timedelta(minutes=flight_length_minutes),
            passengers_amount,
            0,
            airlines,
            airplane_id,
            flight_id
        )
    if random.randint(0, 100) > HUGE_DELAY_CHANCES_IF_DELAY_HAPPENED_PERCENT:
        delay = random.randint(DELAY_MIN_MINUTES, DELAY_MAX_MINUTES)
    else:
        delay = random.randint(HUGE_DELAY_MIN_MINUTES, HUGE_DELAY_MAX_MINUTES)

    return FlightReport(
        planned_start_of_flight[0] + datetime.timedelta(minutes=delay),
        planned_start_of_flight[0] +
        datetime.timedelta(minutes=flight_length_minutes) +
        datetime.timedelta(minutes=delay),
        passengers_amount,
        delay,
        airlines,
        airplane_id,
        flight_id
    )
