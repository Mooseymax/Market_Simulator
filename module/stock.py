from datetime import datetime
from datetime import timedelta

class Stock:
    def __init__(self, name, price, units):
        self.n = name
        self.p = price  # Used for initial value
        self.u = units  # Used for initial value
        
        self.v = units * price
        
        self.c = 0      # Generated cash
        self.r = 0      # 30 day rolling
    
    def sim(self, market, date_a, date_b):
        td = (date_b - date_a).days
        print('Found ' + str(td) + ' days.')
        output = 'date, value' + '\n'
        
        for d in range(0,td):
            self.v = (self.v * (1 + float(market.p[d].c)))
            ''' Simple withdrawal when growing function '''
            if(float(market.p[d].c) > 0.04):
                self.v -= 1000
                self.c += 1000
            if(float(market.p[d].c) < -0.04 and self.c > 0):
                self.v += 1000
                self.c -= 1000
            output += ((date_a + timedelta(days=d)).strftime('%d/%m/%y') + ',' + ('{0:.2f}').format(self.v) + '\n')
        
        with open(self.n + ' output.csv', 'a') as file:
            file.write(output)
        # print(str(d) + '. Price updated: ' + ('{0:.2f}').format(self.p))  # Debugging

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
