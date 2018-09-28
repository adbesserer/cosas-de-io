
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
wordList = []
ult = []

listCSV = csv.reader(fd)
for line in listCSV:
	if (len(line)>1 and len(line)<3) and((line[1][1] >= "A" and line[1][1] <= "Z") or (line[1][1] >= "a" and line[1][1] <= "z")):
		wordList.append(line)
	elif (len(line)==1):
		print(line)
		ult.append(line)        
		#salida.writerow(line)

wordList = sorted(wordList, key=lambda lista: int(lista[0]), reverse=True)

def func(rank,a,b,c):
	return c / ((rank + b) ** a)

cont = 1
ydata, aaaa= map(list, zip(*wordList))
ydata = list(map(int, ydata))
xdata = list(range(len(ydata)))

xdata= xdata[10:]
ydata= ydata[10:]


#for line in wordList:
#	if cont>5 and 1000:
#		xdata.append(float(cont))
#		ydata.append(float(line[0]))
		#print(np.log10(float(line[0])))
#	cont=cont+1

plt.plot(xdata, ydata, 'b-', label='Word frequency distribution NOVELS')
plt.yscale('log')
plt.xscale('log')
popt, pcov = curve_fit(func, xdata, ydata, p0=(1.0,15.0, 100.0), maxfev=1500)
plt.plot(xdata, func(xdata, *popt), 'r-', label='fit curve')


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
for num in popt:
	print(num)
fd.close()
 
