import datetime
import random

from scan import Scan
from scanstage import ScanStage
from utils import random_date


def generate_scan(scan_id: int, scan_stage: ScanStage, ticket_id: int,
                  minimum_scan_date, flight_date):
    return Scan(
        scan_id,
        generate_scan_date(scan_stage, minimum_scan_date, flight_date),
        generate_scan_name(scan_stage),
        ticket_id
    )


# minimum_scan_date =
# previous scan date or
# came to airport date or
# if previous scan was so fast that now passenger must wait to open next gate
def generate_scan_date(scan_stage, prev_scan_date, flight_date):
    # previous generated None - ticket owner was too late
    if prev_scan_date is None:
        return None

    minimum_scan_date = max(flight_date[0] - datetime.timedelta(scan_stage.time_to_enter_in_minutes()),
                  prev_scan_date)
    end = minimum_scan_date + datetime.timedelta(minutes=scan_stage.get_max_wait_time())
    scan_date = random_date(minimum_scan_date, end)
    if scan_date > flight_date[0]:
        return None
    return scan_date


def generate_scan_name(scan_stage):
    return random.choice(scan_stage.get_scan_names())
