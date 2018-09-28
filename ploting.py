import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#novels data by additive novels
#ydata = [6543,10846,12820,17798,23415,24424,25178,25920,27279,32992,38481,52070,56737,57747]
#xdata = [58530,217231,249912,439578,747032,801825,837024,868341,923174,1404403,1714917,2480635,2950880,3120763]

#abstract data by additive folders
ydata= [31418,43929,71456,72905,74009,82530,88020,88655]
xdata= [2594425,3923079,7538908,7998797,8384148,10191409,11507223,11963851]

def func(total, k, b):
	return k*(total**b) 
plt.plot(xdata, ydata, 'b-', label='Heaps Law ABSTRACT corpus')
plt.ylabel('total words')
plt.xlabel('diff words')
popt, pcov = curve_fit(func, xdata, ydata, maxfev=1500)
plt.plot(xdata, func(xdata, *popt), 'r-', label='fit curve')
#plt.yscale('log')
#plt.xscale('log')
for num in popt:
	print(num)
	
plt.legend()
plt.show()