import argparse
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


parser = argparse.ArgumentParser()
parser.add_argument('--path', default=None, required=True, help='path to text file containing words and their frequency')
args = parser.parse_args()
path = args.path


fd = open(path) 
y = 0
n = 0

listCSV = csv.reader(fd)
for line in listCSV:
	if (len(line)>1 and len(line)<3) and((line[1][1] >= "A" and line[1][1] <= "Z") or (line[1][1] >= "a" and line[1][1] <= "z")):
		y = y+int(line[0])
		n = n+1

print(n,y)

fd.close()