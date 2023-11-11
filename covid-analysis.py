import csv
from collections import namedtuple

headers = ("location", "date", "variant", "num_sequences", "perc_sequences", "num_sequences_total")
CovidData = namedtuple('CovidData', field_names=headers)
def read_csv(filename: str) -> CovidData:
    with open(filename) as f:
        _ = f.readline()
        return tuple(map(CovidData._make, csv.reader(f)))
    

data = read_csv("data/covid-variants.csv")
print(data[:10])
