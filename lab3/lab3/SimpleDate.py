class SimpleDate:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.month}/{self.day}"
    
    def __eq__(self, other):
        return (self.month, self.day) == (other.month, other.day)
    
    def __lt__(self, other):
        return (self.month, self.day) < (other.month, other.day)
    
    def __gt__(self, other):
        return (self.month, self.day) > (other.month, other.day)
    
    def getdate(self):
        return self

    def copy(self):
        return SimpleDate(self.month, self.day)
    
    def daysinmonth(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days_in_month[self.month - 1]
    
    def nextday(self):
        if self.day < self.daysinmonth():
            return SimpleDate(self.month, self.day + 1)
        else:
            if self.month == 12:
                return SimpleDate(1, 1)
            else:
                return SimpleDate(self.month + 1, 1)
            
    def daystodate(self, date):
        d = self.copy()
        nod = 0
        while d < date:
            d = d.nextday()
            nod += 1
        return nod
