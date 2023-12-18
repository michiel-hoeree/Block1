import sys
import csv



csvFile = sys.argv[1]
with open(csvFile) as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(', '.join(row)[:10])

