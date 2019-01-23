import datetime
from datetime import timedelta
import random
import re

def daily_rate(r,t):
    if (r >= 0):
        mod = 1
    else:
        mod = -1

    result = ((1 + (abs(r) / 100)) ** (1 / 365)) - 1
    result = result * mod
    return result

def compare_odd(odd, chance):
    if(odd < chance):
        return True
    else:
        return False

def random_rate(t, c, b):
    odds = random.uniform(0,1)
    crash = False
    bull = False
    if(compare_odd(odds, 0.60)):
        # 60%
        rate = daily_rate(random.uniform(-50, 100), t)
    elif(compare_odd(odds, 0.80)):
        # 20%
        rate = daily_rate(random.uniform(-35, 70), t)
    elif(compare_odd(odds, 0.90)):
        # 10%
        rate = daily_rate(random.uniform(-25, 50), t)
    elif(compare_odd(odds, 0.95)):
        # 5%
        rate = daily_rate(random.uniform(-15, 30), t)
    elif(compare_odd(odds, 0.975)):
        # 2.5%
        rate = daily_rate(random.uniform(-45, 30), t)
    elif(compare_odd(odds, 0.99)):
        # 1.5%
        rate = daily_rate(random.uniform(-23, 5), t)
    elif(compare_odd(odds,0.995)):
        # 1% - Market Crash / Low Performance
        rate = daily_rate(random.uniform(-150, -100), t)
        crash = True
    else:
        rate = daily_rate(random.uniform(50, 100), t)
        bull = True
    if(c == True):
        rate = daily_rate(random.uniform(-150, -100), t)
    if(b == True):
        rate = daily_rate(random.uniform(50, 100), t)
    return [rate, crash, bull]

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
frequency = 12

while value_a > value_b:
    crash = False
    crash_count = 0
    
    bull = False
    bull_count = 0
    
    points = 365
    value_a = 100000
    value_b = 0
    rate = random_rate(points, crash, bull)
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
        value_a = growth(value_a, rate[0])
        value_b = growth(value_b, rate[0])
        rate = random_rate(points, crash, bull)
        added += 1
        crash_count += 1
        bull_count += 1
        
        if(rate[1] == True):
            crash = True
        
        if(rate[2] == True):
            bull = True
        
        if(crash_count > 30):
            crash_count = 0
            crash = False
        
        if(bull_count > 30):
            bull_count = 0
            bull = False

    tries += 1
    
    doc_output = ''
    entries = len(output)
    
    for i in output:
        doc_output = doc_output + i + '\n'
    
    with open('output.txt', 'a') as file:
        file.write(re.split(',', output[entries-1])[1] + ' -VS- ' + re.split(',', output[entries-1])[2] + '\n')
        file.write(doc_output)
        file.write('\n')
    
    if(tries > 100):
        print('Exceeded 5,000 scenarios')
        break

print(tries)
for i in output:
    print(i)