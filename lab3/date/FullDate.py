from SimpleDate import *

class FullDate(SimpleDate):
    def __init__(self, year: int, month: int, day: int):
        super().__init__(month, day)
        if year < 1:
            raise ValueError("Year cannot be less than 1")
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")
        if day < 1 or self.daysinmonth() < day:
            raise ValueError("Day must be between 1 and the number of days in the month")
        self.year = year

    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"
    
    def __eq__(self, other):
        return super().__eq__(other) and (self.year == other.year)

    def __lt__(self, other):
        if self.year != other.year:
            return self.year < other.year
        return super().__lt__(other)
    
    def __gt__(self, other):
        if self.year != other.year:
            return self.year > other.year
        return super().__gt__(other)

    def copy(self):
        return FullDate(self.year, self.month, self.day)

    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        return False
    
    def daysinmonth(self):
        if self.month == 2 and self.is_leap_year():
            return 29
        return super().daysinmonth()

    def daystodate(self, date):
        if self > date:
            return date.daystodate(self)  # swap so that it works also for earlier dates

        d = self.copy()
        nod = 0
        while d != date:
            if d.day < d.daysinmonth():
                d.day += 1
            else:
                d.day = 1
                if d.month < 12:
                    d.month += 1
                else:
                    d.month = 1
                    d.year += 1
            nod += 1
        return nod