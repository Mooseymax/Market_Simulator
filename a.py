import datetime
from datetime import timedelta
import random

def refresh_rate():
    odds = random.randint(1,1000)
    if(odds > 1000):
        rate = random.uniform(-30,2)
    elif(odds > 950):
        rate = random.uniform(-7,10)
    elif(odds > 850):
        rate = random.uniform(-4,5)
    elif(odds > 650):
        rate = random.uniform(-2.5,3)
    elif(odds > 350):
        rate = random.uniform(-1,1.5)
    else:
        rate = random.uniform(-0.5,1)
    return rate / 100

def add_day(date):
    date += datetime.timedelta(days=1)
    return date

def growth(val):
    val += (val * rate)
    return val

value_a = 100000
value_b = 0    
test = []
loop = 0

while value_a > value_b:
    points = 12
    value_a = 100000
    value_b = 0
    rate = 0.01
    regular = value_a / points
    test = []

    today = datetime.datetime.today()

    for i in range(0,points):
        value_b += regular
        d = today
        v = value_a
        m = value_b
        test.append(d.strftime("%d/%m/%y") + ',' + "{0:.2f}".format(v) + ',' + "{0:.2f}".format(m))
        #print(d.strftime("%d/%m/%y") + ',' + "{0:.2f}".format(v) + ',' + "{0:.2f}".format(m))
        today = add_day(today)
        value_a = growth(value_a)
        value_b = growth(value_b)
        rate = refresh_rate()
    loop += 1
    if(loop > 5000):
        print('Exceeded 5,000 scenarios')
        break

print(loop)
for i in test:
    print(i)
'''
for i in range(0,points):
    value += regular
    d = today
    v = value
    print(d.strftime("%d/%m/%y") + ',' + "{0:.2f}".format(v))
    today = add_day(today)
    value = growth(value)
    rate = refresh_rate()
'''