import csv
from pprint import pprint
from collections import namedtuple, defaultdict
from itertools import groupby, zip_longest
from functools import reduce

import numpy as np
import matplotlib.pyplot as plt

filename = "data/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv"
year = 2015
def file_headers(filename):
    with open(filename, mode='r') as csv_file:
        return csv_file.readline() 

WeatherData = namedtuple('WeatherData', field_names=file_headers(filename))
WeatherAnalysed = defaultdict()


def read_data(filename):
    with open(filename, mode='r') as csv_file:
        _headers = csv_file.readline() 
        # return tuple(map(WeatherData._make, csv.reader(csv_file)))
        return tuple(map(lambda x: WeatherData(x[0], x[1], x[2], float(x[3])), csv.reader(csv_file)))  # besoin de spécifier le type de la 4ème colonne ... TODO: Trouver mieux

def groupe_max(acc, val):
    day = val['day']
    data_value = val['Data_Value']
    if day not in acc:
        acc[day] = data_value
    else:
        acc[day] = max(acc[day], data_value)
    return acc

def groupe_min(acc, val):
    day = val['day']
    data_value = val['Data_Value']
    if day not in acc:
        acc[day] = data_value
    else:
        acc[day] = min(acc[day], data_value)
    return acc

# TODO: Compressser toutes ces actions en une
data = read_data(filename)
data = tuple(sorted(data, key= lambda x: x.Date))
data = tuple(map(lambda x: WeatherData(x.ID, x.Date, x.Element, x.Data_Value * 0.1), data))
data = tuple(map(lambda x: {'ID': x.ID, 'Date': x.Date, 'Element': x.Element, 'Data_Value': x.Data_Value, 'Year': int(x.Date[:4]), 'day': x.Date[5:]}, data))

_0514 = tuple(filter(lambda x: x['Year'] != year, data))
_15 = tuple(filter(lambda x: x['Year'] == year, data))

# groupby par jour et maximum/minimum de température sur cette journée
max_0514 = reduce(groupe_max, _0514, {})
min_0514 = reduce(groupe_min, _0514, {})

max_15 = reduce(groupe_max, _15, {})
min_15 = reduce(groupe_min, _15, {})

max_all = tuple(map(lambda args: {'day': args[0], '2005-2014': args[1], '2015': args[2]}, zip_longest(max_0514.keys(), max_0514.values(), max_15.values(), fillvalue=0)))  # Pas de 29/02 en 2015, on remplit par un 0
min_all = tuple(map(lambda args: {'day': args[0], '2005-2014': args[1], '2015': args[2]}, zip_longest(min_0514.keys(), min_0514.values(), min_15.values(), fillvalue=0)))

max_record_15 = tuple(filter(lambda x: x['2015'] > x['2005-2014'], max_all))
min_record_15 = tuple(filter(lambda x: x['2015'] < x['2005-2014'], min_all))


day_to_int = {day: num_day for day, num_day in zip(max_0514.keys(), list(range(366)))}

plt.figure(figsize=(10,10))

plt.plot(max_0514.values(), 
         c = 'red', 
         label ='Record High')

plt.plot(min_0514.values(), 
         c = '#00FFFF', 
         label ='Record Low')


plt.scatter([day_to_int[day_rec['day']] for day_rec in max_record_15], 
            [value["2015"] for value in max_record_15], 
            c = 'black', 
            label = "Record Breaking High in "+ str(year))

print([day_to_int[day_rec['day']] for day_rec in min_record_15])
plt.scatter([day_to_int[day_rec['day']] for day_rec in min_record_15], 
            [value["2015"] for value in min_record_15], 
            c = 'blue', 
            label = "Record Breaking Low in " + str(year))


print(len(np.array(list(max_0514.values()))))
plt.xlabel('Days of the year', fontsize=10)
plt.ylabel('Temperature (Celsius)', fontsize=10)
plt.title('Michigan Record Temperatures between 2005 and 2015', fontsize=15)

plt.gca().fill_between(range(len(max_0514.values())), 
                       np.array(list(max_0514.values())).reshape(len(max_0514.values()),), 
                       np.array(list(min_0514.values())).reshape(len(min_0514.values()),), 
                       facecolor='purple', alpha=0.1)

plt.show()
