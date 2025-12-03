from OilWell import *
import statistics

class OilField:
    def __init__(self, filepath):
        self.oil_wells = []
        self.a = 0

        with open(filepath, 'r') as file:
            for line in file:
                id, x, y = line.strip().split(',')
                well = OilWell(id, float(x), float(y))
                self.oil_wells.append(well)

    def find(self):
        self.oil_wells.sort()

        well_ys = [well.y for well in self.oil_wells]

        self.a = statistics.median(well_ys)

        return self.a
    
    def pipelength(self):
        total_length = 0
        for well in self.oil_wells:
            total_length += abs(well.y - self.a)
        return total_length