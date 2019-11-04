from enum import Enum


class ScanStage(Enum):
    BAGGAGE = {'time_to_enter_minutes': 150, 'max_wait_time': 30,
               'names': ["BG_PRZEMEK", "BG_ANDRZEJ", "BG_ANIA"]}
    DUTY_FREE = {'time_to_enter_minutes': 120, 'max_wait_time': 90,
                 'names': ["DT_TOMEK", "DT_ROBERT", "DT_KLAUDIA"]}
    AIRPLANE = {'time_to_enter_minutes': 30, 'max_wait_time': 30,
                'names': ["AR_ZUZA", "AR_MACIEK", "AR_WERA"]}

    def time_to_enter_in_minutes(self):
        return self.value['time_to_enter_minutes']

    def get_scan_names(self):
        return self.value['names']

    def get_max_wait_time(self):
        return self.value['max_wait_time']
