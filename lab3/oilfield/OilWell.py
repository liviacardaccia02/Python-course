class OilWell:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.y < other.y
