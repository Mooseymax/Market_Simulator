import datetime
from datetime import timedelta
import csv
from module.stock import Stock, Market

# Historic Files
DAX = 'DAX.csv'
DOW = 'Dow.csv'
FTSE = 'FTSE.csv'

# Output File
OUTPUT = 'output.txt'

def import_csv(file_name):
    data = []
    with open(file_name) as file:
        reader = csv.reader(file)
        data = list(reader)
        return(data)

# Import historic stock performance
Dax_data = import_csv(DAX)
Dow_data = import_csv(DOW)
Ftse_data = import_csv(FTSE)

Ftse = Market('FTSE', Ftse_data)

'''
for i in Ftse.p:
    print(i.d)
'''

starting_value = 100000

vanguard = Stock('Vanguard', 1, starting_value)

