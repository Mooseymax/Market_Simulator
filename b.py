import datetime
from datetime import timedelta
import random

def daily_rate(r):
    if (r >= 0):
        mod = 1
    else:
        mod = -1
    
    result = pow((1 + abs(r)), 1 / 365) - 1
    result = result * mod
    return result

def compare_odd(odd, chance):
    if(odd < chance):
        return True
    else:
        return False

def random_rate():
    odds = random.uniform(0,1)
    if(compare_odd(odds, 0.60)):
        # 60%
        rate = daily_rate(random.uniform(-15.46, 26.33))
    elif(compare_odd(odds, 0.80)):
        # 20%
        rate = daily_rate(random.uniform(-18.42, 30.26))
    elif(compare_odd(odds, 0.90)):
        # 10%
        rate = daily_rate(random.uniform(-21.22, 34.35))
    elif(compare_odd(odds, 0.95)):
        # 5%
        rate = daily_rate(random.uniform(-24.02, 38.45))
    elif(compare_odd(odds, 0.975)):
        # 2.5%
        rate = daily_rate(random.uniform(-26.86, 42.49))
    elif(compare_odd(odds, 0.99)):
        # 1.5%
        rate = daily_rate(random.uniform(-29.75, 46.50))
    else:
        # 1% - Market Crash / Low Performance
        rate = daily_rate(random.uniform(-30.00, 3.00))
    return rate

def add_day(date):
    date += datetime.timedelta(days=1)
    return date

def growth(val, rate):
    val += (val * rate)
    return val

value_a = 100000
value_b = 0
tries = 0
output = []
frequency = 52

while value_a > value_b:
    points = 365
    value_a = 100000
    value_b = 0
    rate = random_rate()
    regular = value_a / frequency
    
    often = points / frequency
    added = often
    
    output = []
    d = datetime.datetime.today()
    
    for i in range(0, points):
        if(added >= often):
            value_b += regular
            added = 0
        output.append(d.strftime("%d/%m/%y") + ',' +
                        "{0:.2f}".format(value_a) + ',' +
                        "{0:.2f}".format(value_b))
        d = add_day(d)
        value_a = growth(value_a, rate)
        value_b = growth(value_b, rate)
        rate = random_rate()
        added += 1
    tries += 1
    if(tries > 5000):
        print('Exceeded 5,000 scenarios')
        break

print(tries)
for i in output:
    print(i)