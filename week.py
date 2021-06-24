from enum import Enum


class Week(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    def __int__(self):
        return self.value

    def __str__(self):
        return self.name.capitalize()

