import sys
import csv



csvFile = sys.argv[1]
with open(csvFile) as csvfile:
    pokemons = csv.reader(csvfile,delimiter=';')
    for row in pokemons:
        if row[1] == "2":
            print(f"{row[0]} is een gen {row[1]} pokemon")

