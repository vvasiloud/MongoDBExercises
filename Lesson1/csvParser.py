import os
from pprint import pprint
import csv

DATADIR = ""
DATAFILE = "file.csv"


def parse_file(datafile):     
    data = []
    with open(datafile, "r") as f: 
        reader = csv.DictReader(f)
        for line in reader:
            data.append(line)
        pprint(data)

    return data
