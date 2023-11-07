#!/bin/bash

# Petit script pour mesurer le temps d'execution moyen d'un script python
if [ $# -eq 0 ]; then
    echo "Utilisation : ./timeit_ipython.sh monscript.py"
    exit 1
fi

script=$1  # script à exécuter
shift  # Suppression le premier argument (nom du script) de la liste des arguments

ipython -c "%timeit %run $script $@"
