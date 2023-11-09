# Python fonctionnel

Ce répertoire vise à explorer le côté fonctionnel de Python, notamment pour l'analyse de données.
Pour premier exemple, l'analyse de données métérologiques en mimiquant le [code `pandas` écrit par LoPzeous](https://github.com/LoPezous/Weather-analysis).
L'idée est de performer cette analyse en pure Python, et en suivant les principes de programmation fonctionnelle ; notamment l'immutabilité des structures de
données, et la transofrmation des données par de simples fonctions mathématiques.

## Implémentation en SQL

Une implémentation est disponible en SQL, comme simple exemple d'exploration. Pour utiliser le script SQL, assurez-vous d'avoir `sqlite3` installé, puis
lancez la commande

```console
sqlite3 data/weatherdata.db < weather-analysis.sql
``````

puis pour extraire les résultats des tableaux `max_records_15`

```console
sqlite3 -header -csv data/weatherdata.db "select * from max_record_15;" > data/max_records_15.csv
``````

puis `min_records_15`

```console
sqlite3 -csv data/weatherdata.db "select * from min_record_15;" > data/min_records_15.csv
``````

Les arguments `-header` et `-csv` permettent respectivement d'afficher les en-têtes de la table, et de séparer les valeurs par des virgules.

Alternativement, le script `get_data.sh` se charge de lancer ces deux commandes. Pour le lancer, s'assurer que le script est exécutable

```console
chmod +x get_data.sh
````

puis simplement

```console
./get_data.sh
````
