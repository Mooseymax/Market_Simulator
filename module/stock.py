from datetime import datetime
from datetime import timedelta
import random

withdrawal = False

def random_rate(modifier):
    roll = random.uniform(0,1)
    m = modifier    # Positive modifier
    n = 1 - m       # Negative modifier
    
    ''' Add in a bull run or market crash on 9% '''
    
    if(roll > 0.25):
        rate = random.uniform(-0.01 * n, 0.01 * m)  # 1% up or down
    elif(roll > 0.10):
        rate = random.uniform(-0.02 * n, 0.02 * m)  # 2% up or down
    elif(roll > 0.04):
        rate = random.uniform(-0.03 * n, 0.03 * m)  # 3% up or down
    elif(roll > 0.02):
        rate = random.uniform(-0.04 * n, 0.04 * m)  # 4% up or down
    elif(roll > 0.01):
        rate = random.uniform(-0.05 * n, 0.05 * m)  # 5% up or down
    elif(roll > 0.004):
        rate = random.uniform(-0.06 * n, 0.06 * m)  # 6% up or down
    elif(roll > 0.002):
        rate = random.uniform(-0.07 * n, 0.07 * m)  # 7% up or down
    elif(roll > 0.001):
        rate = random.uniform(-0.08 * n, 0.08 * m)  # 8% up or down
    else:
        rate = random.uniform(-0.09 * n, 0.09 * m)  # 9% up or down
    return rate

class Stock:
    def __init__(self, name, price, units):
        self.n = name
        self.p = price  # Used for initial value
        self.u = units  # Used for initial value
        
        self.v = units * price
        
        self.c = 0      # Generated cash
        self.r = 0      # 30 day rolling
    
    def sim(self, market, date_a, date_b):
        start_number = 0
        for i in market.p:
            if(i.d.date() == date_a or 
                i.d.date() + timedelta(days=1) == date_a or 
                i.d.date() + timedelta(days=2) == date_a or 
                i.d.date() + timedelta(days=3) == date_a):
                break
            else:
                start_number += 1
        #print('Starting at position ' + str(start_number))
        
        td = (date_b - date_a).days
        #print('Found ' + str(td) + ' days.')
        output = 'date, value' + '\n'
        
        for d in range(start_number,start_number + td):
            self.v = (self.v * (1 + float(market.p[d].c)))
            ''' Simple withdrawal when growing function '''
            if(withdrawal == True):
                if(float(market.p[d].c) > 0.02):
                    self.v -= 1000
                    self.c += 1000
                if(float(market.p[d].c) < -0.02 and self.c > 0):
                    self.v += 1000
                    self.c -= 1000
            ''' End of withdrawal function '''
            output += ((date_a + timedelta(days=d)).strftime('%d/%m/%Y') + ',' + ('{0:.2f}').format(self.v) + '\n')
        
        with open(self.n + ' output.csv', 'w') as file:
            file.write(output)
        # print(str(d) + '. Price updated: ' + ('{0:.2f}').format(self.p))  # Debugging

class Market:
    def __init__(self, name, data):
        self.n = name
        self.d = data
        self.p = []
        
        if(len(self.d) > 1):
            for row in self.d[1:]:
                self.p.append(self.Data(datetime.strptime(row[0], '%d/%m/%Y'), row[6]))
        else:
            print('Generating random market movements.')
            #days = int(input('How many days? '))
            days = 2000
            for i in range(0,days):
                self.p.append(self.Data(datetime.today().date() + timedelta(days=i), random_rate(0.53)))
    
    class Data:
        def __init__(self, date, change):
            self.d = date
            self.c = change
