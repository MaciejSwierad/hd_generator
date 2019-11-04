class Scan:
    def __init__(self, scan_id, scan_date, scanner_name, ticket_id):
        self.id = scan_id
        self.scan_date = scan_date
        self.scanner_name = scanner_name
        self.ticket_id = ticket_id

    def __str__(self) -> str:
        string_date_of_scan = ""
        if self.scan_date is not None:
            string_date_of_scan = self.scan_date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            string_date_of_scan = 'TOO_LATE'
        return f" {self.id} {string_date_of_scan} {self.scanner_name} {self.ticket_id}"
