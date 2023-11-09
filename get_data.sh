#!/bin/bash

# Note: avoid headers to easily open with numpy and plot
sqlite3 -header -csv data/weatherdata.db "select * from max_record_15;" > data/max_records_15.csv
echo "Résultats écrits dans le fichier 'data/max_records_15.csv'"

sqlite3 -header -csv data/weatherdata.db "select * from min_record_15;" > data/min_records_15.csv
echo "Résultats écrits dans le fichier 'data/min_records_15.csv'"

sqlite3 -header -csv data/weatherdata.db "select * from max_0514;" > data/max_0514.csv
echo "Résultats écrits dans le fichier 'data/max_0514.csv'"

sqlite3 -header -csv data/weatherdata.db "select * from min_0514;" > data/min_0514.csv
echo "Résultats écrits dans le fichier 'data/min_0514.csv'"

sqlite3 -header -csv data/weatherdata.db "select * from min_0514;" > data/min_0514.csv
echo "Résultats écrits dans le fichier 'data/min_0514.csv'"
