import datetime
import random
import string
from random import uniform

import names

from flight_generator import MIN_FLIGHT_DATE
from ticket import Ticket
from utils import random_date

MAX_PRICE = 8000.0
MIN_PURCHASE_DATE = datetime.datetime(2013, 1, 1)
MIN_BIRTH_DATE = datetime.datetime(1940, 1, 1)
DOCUMENT_TYPES = ["IDC", "PAS"]


def generate_ticket(ticket_id: int, flight_id: int, airplane_id: int, flight_date):
    return Ticket(
        ticket_id,
        generate_price(),
        generate_birth_date(),
        flight_date,
        generate_purchase_date(flight_date),
        generate_document_id(),
        ticket_id,
        flight_id,
        airplane_id,
        generate_name(),
        generate_surname(),
        generate_document_type(),
        generate_sex()
    )


def generate_birth_date():
    return random_date(MIN_BIRTH_DATE, MIN_FLIGHT_DATE)


def generate_price():
    return round(uniform(9.0, MAX_PRICE), 2)


def generate_purchase_date(flight_date):
    end = datetime.datetime.now()
    return random_date(MIN_PURCHASE_DATE, min(flight_date[0], end))


def generate_document_id():
    letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    numbers = ''.join(random.choice(string.digits) for _ in range(6))
    return letters + numbers


def generate_name():
    return names.get_first_name()


def generate_surname():
    return names.get_last_name()


def generate_document_type():
    return random.choice(DOCUMENT_TYPES)


def generate_sex():
    a = random.randint(0, 1)
    if a == 0:
        return "MEZCZYZNA"
    return "KOBIETA"
