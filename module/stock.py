from datetime import datetime

class Stock:
    def __init__(self, name, price, units):
        self.n = name
        self.p = price
        self.u = units

class Market:
    def __init__(self, name, data):
        self.n = name
        self.d = data
        self.p = []
        
        for row in self.d[1:]:
            self.p.append(self.Data(row[0], row[6]))
        
    
    class Data:
        def __init__(self, date, change):
            self.d = date
            self.c = change