import csv
from collections import namedtuple, defaultdict
from itertools import groupby, zip_longest
from functools import reduce

import numpy as np
import matplotlib.pyplot as plt

PLOT = False

filename = "data/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv"
year = 2015


new_headers = ("ID", "Date", "Element", "Data_Value", "Year", "day",)
WeatherAnalysed = namedtuple('WeatherAnalysed', field_names=new_headers)


def read_data(filename):
    with open(filename, mode='r') as csv_file:
        _headers = csv_file.readline()
        WeatherData = namedtuple('WeatherData', field_names=_headers)
        return tuple(map(WeatherData._make, csv.reader(csv_file)))


def groupe_max(acc, val):
    day = val.day
    acc[day] = max(acc[day], val.Data_Value)
    return acc

def groupe_min(acc, val):
    day = val.day
    acc[day] = min(acc[day], val.Data_Value)
    return acc

# Note, comparaison avec le code en Pandas: Ce code-ci est beaucoup plus lent pour ouvrir et surtout créer la table de données. 
# Trouver une structure de données bien pensée qui pourrait compler ce déficit.
# Le reste du code semble équivalent en vitesse, voire avec un léger avantage pour celui-ci. 


# Transforme le jeu de données initial en 'WeatherAnalysed' pour contenir 'Year' et 'day'
data = read_data(filename)
data = tuple(map(lambda x: WeatherAnalysed(x.ID, x.Date, x.Element, float(x.Data_Value) * 0.1, int(x.Date[:4]), x.Date[5:]), read_data(filename)))
data = tuple(sorted(data, key= lambda x: x.day))
_0514 = tuple(filter(lambda x: x.Year != year, data))
_15 = tuple(filter(lambda x: x.Year == year, data))

# groupby par jour et maximum/minimum de température sur cette journée
max_0514 = reduce(groupe_max, _0514, defaultdict(lambda : -100))  # on veut que la valeur par défaut soit remplacée par le max, donc on prend une température impossiblement basse
min_0514 = reduce(groupe_min, _0514, defaultdict(lambda: 100))

max_15 = reduce(groupe_max, _15, defaultdict(lambda: -100))
min_15 = reduce(groupe_min, _15, defaultdict(lambda: 100))

# TODO: Arranger cette partie pour accéder plus facilement aux données
max_all = tuple(map(lambda args: {'day': args[0], '2005-2014': args[1], '2015': args[2]}, zip_longest(max_0514.keys(), max_0514.values(), max_15.values(), fillvalue=0)))  # Pas de 29/02 en 2015, on remplit par un 0
min_all = tuple(map(lambda args: {'day': args[0], '2005-2014': args[1], '2015': args[2]}, zip_longest(min_0514.keys(), min_0514.values(), min_15.values(), fillvalue=0)))

max_record_15 = tuple(filter(lambda x: x['2015'] > x['2005-2014'], max_all))
min_record_15 = tuple(filter(lambda x: x['2015'] < x['2005-2014'], min_all))


if PLOT:
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

    plt.xlabel('Days of the year', fontsize=10)
    plt.ylabel('Temperature (Celsius)', fontsize=10)
    plt.title('Michigan Record Temperatures between 2005 and 2015', fontsize=15)

    plt.gca().fill_between(range(len(max_0514.values())), 
                        np.array(list(max_0514.values())).reshape(len(max_0514.values()),), 
                        np.array(list(min_0514.values())).reshape(len(min_0514.values()),), 
                        facecolor='purple', alpha=0.1)

    plt.show()
