import datetime
import random
import names

import ticket_generator
from baggage_generator import generate_baggage
from baggege_type import BaggageType
from flight_generator import generate_flight
from flight_ticket_generator import generate_flight_ticket
from flightreport_generator import generate_flight_report
from scan_generator import generate_scan
from scanstage import ScanStage

NUMBER_OF_FLIGHTS = 2
MIN_AMOUNT_OF_SITS = 60
MAX_AMOUNT_OF_SITS = 140

T2_NUMBER_OF_FLIGHTS = 1
T2_PROBABILITY_PERCENT = 20


#NUMBER_OF_FLIGHTS = 100
#MIN_AMOUNT_OF_SITS = 100
#MAX_AMOUNT_OF_SITS = 300

PROBABILITY_TO_HAVE_EACH_BAGGAGE_TYPE_PERCENTS = 35
PROBABILITY_FOR_PASSENGER_TO_RESIGN_PROMILES = 2
PROBABILITY_NOT_TO_BUY_TICKET_PROMILES = 2
PROBABILITY_FOR_PASSENGER_TO_CHANGE_SURNAME_PROMILES = 1

PASSENGER_COME_TO_THE_AIRPORT_BEFORE_FLIGHT_IN_MINUTES_MIN = 100
PASSENGER_COME_TO_THE_AIRPORT_BEFORE_FLIGHT_IN_MINUTES_MAX = 180

f = open("dane.txt", "w")
f2 = open("danet2.txt", "w")
csv = open("raport.csv", "w")
current_file = f
willSurnameBeChanged = False
#f.write("hehe")


def generate_with_baggage():
    return random.randint(0, 100) < PROBABILITY_TO_HAVE_EACH_BAGGAGE_TYPE_PERCENTS


def generate_with_purchased_ticket():
    return random.randint(0, 1000) > PROBABILITY_NOT_TO_BUY_TICKET_PROMILES


def generate_with_new_surname():
    return random.randint(0, 1000) < PROBABILITY_FOR_PASSENGER_TO_CHANGE_SURNAME_PROMILES


def generate_with_T2():
    return random.randint(0, 100) < T2_PROBABILITY_PERCENT


def generate_purchased_ticket(global_ticket_id, flight, flight_ticket):
    ticket = ticket_generator.generate_ticket(
        global_ticket_id, flight.flight_id, flight.airplane_id,
        flight.flight_start_date
    )
    flight_ticket.ticket_id = ticket.db_id
    #print("TICKET: " + ticket.__str__())
    current_file.write(
        "INSERT INTO BILET (id, cena, data_urodzenia, data_wylotu, data_zakupu, id_dokumentu, identyfikator_biletu,"
        "identyfikator_lotu, identyfikator_samolotu, imie, nazwisko, rodzaj_dokumentu, plec)"
        " VALUES ({}, {}, '{}', '{}', '{}', '{}', {}, {}, {}, '{}', '{}', '{}', '{}')\n".format(ticket.db_id, ticket.price, ticket.date_of_birth,
                                                                            ticket.date_of_flight[0], ticket.date_of_purchase,
                                                                            ticket.document_id, ticket.ticket_id, ticket.flight_id,
                                                                            ticket.airplane_id, ticket.name, ticket.surname, ticket.document_type, ticket.plec))
    return ticket


def generate_baggages(baggage_id, global_ticket_id):
    baggages = []
    for b in BaggageType:
        if generate_with_baggage():
            new_baggage = generate_baggage(baggage_id, global_ticket_id, b)
            baggages.append(new_baggage)
            baggage_id += 1
            #print("BAGGAGE: " + new_baggage.__str__())
            current_file.write(
                "INSERT INTO BAGAZ (id, masa, rodzaj, fk_bilet)"
                """ VALUES ({}, {}, '{}', {})\n""".format(new_baggage.db_id, new_baggage.weight,
                                                    new_baggage.type, new_baggage.ticket_id))
    return baggages


def generate_scans(global_scan_id, has_baggage, ticket_id, flight_date):
    scans = []
    random_minutes = random.randint(PASSENGER_COME_TO_THE_AIRPORT_BEFORE_FLIGHT_IN_MINUTES_MIN,
                                    PASSENGER_COME_TO_THE_AIRPORT_BEFORE_FLIGHT_IN_MINUTES_MAX)
    coming_to_airport_date = flight_date[0] - datetime.timedelta(minutes=random_minutes)

    scan = None
    if random.randint(0, 1000) > PROBABILITY_FOR_PASSENGER_TO_RESIGN_PROMILES:
        if has_baggage:
            scan = generate_scan(
                global_scan_id, ScanStage.BAGGAGE, ticket_id, coming_to_airport_date, flight_date
            )
            scans.append(scan)
            global_scan_id += 1
            #print("SCAN: " + scan.__str__())
            current_file.write(
                "INSERT INTO SKAN (id, data, nazwa_czujnika, fk_bilet)"
                """ VALUES ({}, '{}', '{}', {})\n""".format(scan.id, scan.scan_date, scan.scanner_name, scan.ticket_id))

    if scan is None:
        scan = generate_scan(
            global_scan_id, ScanStage.DUTY_FREE, ticket_id, coming_to_airport_date, flight_date
        )
    else:
        scan = generate_scan(
            global_scan_id, ScanStage.DUTY_FREE, ticket_id, scan.scan_date, flight_date
        )
    scans.append(scan)
    global_scan_id += 1
    #print("SCAN: " + scan.__str__())
    current_file.write(
        "INSERT INTO SKAN (id, data, nazwa_czujnika, fk_bilet)"
        " VALUES ({}, '{}', '{}', {})\n".format(scan.id, scan.scan_date, scan.scanner_name, scan.ticket_id))

    scan = generate_scan(
        global_scan_id, ScanStage.AIRPLANE, ticket_id, scan.scan_date, flight_date
    )

    scans.append(scan)
    global_scan_id += 1
    #print("SCAN: " + scan.__str__())
    current_file.write(
        "INSERT INTO SKAN (id, data, nazwa_czujnika, fk_bilet)"
        " VALUES ({}, '{}', '{}', {})\n".format(scan.id, scan.scan_date, scan.scanner_name, scan.ticket_id))

    return scans


def generate_passenger_process(global_ticket_id, flight, flight_ticket, baggage_id, global_scan_id,
                               flight_date):
    ticket = generate_purchased_ticket(global_ticket_id, flight, flight_ticket)
    baggage = generate_baggages(baggage_id, global_ticket_id)
    scans = generate_scans(global_scan_id, baggage.__len__() > 0, global_ticket_id, flight_date)
    return ticket, baggage, scans


def generation_process():
    global_ticket_id = 1
    global_baggage_id = 1
    global_scan_id = 1

    for i in range(1, NUMBER_OF_FLIGHTS + T2_NUMBER_OF_FLIGHTS + 1):
    #for i in range(1, NUMBER_OF_FLIGHTS + 1):
        global current_file
        global willSurnameBeChanged
        if i > NUMBER_OF_FLIGHTS:
            current_file = f2

        flight = generate_flight(i)
        #print('FLIGHT: ' + flight.__str__())
        current_file.write(
            "INSERT INTO LOT (id, data_przylotu, data_wylotu, identyfikator_lotu, identyfikator_samolotu, linia_lotnicza, miejsce_przylotu, miejsce_wylotu)"
            " VALUES ({}, '{}', '{}', {}, {}, '{}', '{}', '{}')\n".format(flight.db_id, flight.flight_end_date, flight.flight_start_date[0],
                                                                flight.flight_id, flight.airplane_id, flight.airline,
                                                                flight.to_place, flight.from_place))
        number_of_sits = random.randint(MIN_AMOUNT_OF_SITS, MAX_AMOUNT_OF_SITS)
        prev_sit = None
        passengers_amount = 0
        for j in range(1, number_of_sits + 1):

            flight_ticket = generate_flight_ticket(global_ticket_id, prev_sit, flight.airline, flight.db_id)
            prev_sit = flight_ticket.row_number, flight_ticket.place_number
            if generate_with_purchased_ticket():
                if generate_with_T2():
                    current_file = f2
                ticket, baggage, scans = generate_passenger_process(
                    global_ticket_id, flight, flight_ticket, global_baggage_id,
                    global_scan_id, flight.flight_start_date
                )
                global_baggage_id += baggage.__len__()
                global_scan_id += scans.__len__()
                passengers_amount += 1
            #print("TICKET FLIGHT: " + flight_ticket.__str__())
            current_file.write("INSERT INTO BILET_LOT (id, miejsce, rzad, fk_bilet, fk_lot_linia_lotnicza, fk_lot_identyfikator_lotu)"
                    " VALUES ({}, {}, {}, {}, '{}', {})\n".format(flight_ticket.db_id, flight_ticket.place_number, flight_ticket.row_number, flight_ticket.ticket_id, flight_ticket.airlines, flight_ticket.flight_id))
            global_ticket_id += 1
            if i < NUMBER_OF_FLIGHTS:
                current_file = f

            if generate_with_new_surname():
                last_file = current_file
                current_file = f2
                current_file.write(
                    "INSERT INTO BILET (id, cena, data_urodzenia, data_wylotu, data_zakupu, id_dokumentu, identyfikator_biletu,"
                    "identyfikator_lotu, identyfikator_samolotu, imie, nazwisko, rodzaj_dokumentu)"
                    " VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})\n".format(global_ticket_id, ticket.price,
                                                                                        ticket.date_of_birth,
                                                                                        ticket.date_of_flight[0],
                                                                                        ticket.date_of_purchase,
                                                                                        ticket.document_id,
                                                                                        global_ticket_id,
                                                                                        ticket.flight_id,
                                                                                        ticket.airplane_id, ticket.name,
                                                                                        names.get_last_name(),
                                                                                        ticket.document_type))
                current_file.write(
                    "INSERT INTO BILET_LOT (id, miejsce, rzad, bilet_id, fk_lot_linia_lotnicza, fk_lot_identyfikator_biletu)"
                    " VALUES ({}, {}, {}, {}, {}, {})\n".format(global_ticket_id, flight_ticket.place_number,
                                                                flight_ticket.row_number, global_ticket_id,
                                                                global_ticket_id, flight_ticket.airlines))
                current_file.write(
                    "INSERT INTO SKAN (id, data, nazwa_czujnika, fk_bilet)"
                    " VALUES ({}, '{}', '{}', {})\n".format(global_scan_id, scans[0].scan_date, scans[0].scanner_name, global_ticket_id))
                global_scan_id += 1
                current_file.write(
                    "INSERT INTO SKAN (id, data, nazwa_czujnika, fk_bilet)"
                    " VALUES ({}, '{}', '{}', {})\n".format(global_scan_id, scans[1].scan_date, scans[1].scanner_name,
                                                        global_ticket_id))

                if baggage.__len__():
                    current_file.write(
                        "INSERT INTO BAGAZ (id, masa, rodzaj, fk_bilet)"
                        " VALUES ({}, {}, {}, {})\n".format(global_baggage_id, baggage[0].weight,
                                                            baggage[0].type, global_ticket_id))
                    global_baggage_id += 1
                global_scan_id += 1
                global_ticket_id += 1
                current_file = last_file

        report = generate_flight_report(flight.flight_start_date, (int)(
            (flight.flight_end_date - flight.flight_start_date[0]).seconds / 60), passengers_amount,
                                        flight.airline, flight.airplane_id, flight.flight_id)
        #to jest csv
        print("FLIGHT REPORT: " + report.__str__())
        csv.write(report.__str__())

generation_process()

f.close()
f2.close()
