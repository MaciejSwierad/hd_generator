import datetime
import random

from flight import Flight
from utils import random_date

MAX_FLIGHT_DATE = datetime.datetime(2021, 1, 1)
MIN_FLIGHT_DATE = datetime.datetime(2015, 1, 1)
MIN_FLIGHT_LENGTH = 120
MAX_FLIGHT_LENGTH = 480


def generate_flight(flight_id: int):
    flight_date = generate_flight_date(),
    return Flight(
        flight_id,
        flight_date,
        generate_end_flight_date(flight_date),
        flight_id,
        generate_airplane_id(),
        generate_airline(),
        generate_place(),
        generate_place()
    )


def generate_flight_date():
    return random_date(MIN_FLIGHT_DATE, MAX_FLIGHT_DATE)


def generate_end_flight_date(flight_date: datetime):
    return flight_date[0] + datetime.timedelta \
        (minutes=random.randint(MIN_FLIGHT_LENGTH, MAX_FLIGHT_LENGTH))


def generate_airplane_id():
    return random.randint(1, 1000)


def generate_airline():
    return random.choice(
        ["Adria Airways", "Blue Air", "Cathay Pacific", "Ryanair", "Wizzair", "Lufthansa",
         "Delta Airlines", "Finnair", "Lot", "Flydubai", "JetBlue", "Koral Blue",
         "Norwegian Air", "Onur Air", "SAS"]
    )


def generate_place():
    return random.choice(
        ["Londyn", "Turku", "Dubaj", "Belfast", "Berlin", "Malta", "Santorini", "Sycylia", "Dublin",
         "Kolonia", "Ejlat", "Edynburg", "Walencja", "Marsylia", "Bangkok", "Phuket"]
    )
