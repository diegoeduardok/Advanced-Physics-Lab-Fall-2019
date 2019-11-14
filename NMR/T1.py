import numpy as np 
from scipy.optimize import curve_fit as fit 
from matplotlib import pyplot as plt

def exponential(x, c0, tau, c1):
	return c0*(1 - np.exp(-x*tau)) + c1

#Water data
x =[0.0001,
	0.01,
	0.02,
	0.03,
	0.032,
	0.034,
	0.036,
	0.038,
	0.039,
	0.04,
	0.041,
	0.045,
	0.047,
	0.05,
	0.06,
	0.07,
	0.08,
	0.1,
	0.2,
	0.3,
	0.5]

y =[-1.17,
	-0.788,
	-0.485,
	-0.261,
	-0.225,
	-0.193,
	-0.164,
	-0.136,
	-0.126,
	-0.119,
	0,
	0.13,
	0.152,
	0.18,
	0.299,
	0.385,
	0.462,
	0.58,
	0.878,
	1,
	1.1]



'''
#Heavy mineral oil data
x = [0.0001,
0.001,
0.01,
0.03,
0.1,
0.3,
0.7,
1,
1.1,
1.2,
1.3,
1.32,
1.4,
1.6,
1.8,
2,
3,
4,
5,
6,
7,
8]

y = [-1.53,
-1.54,
-1.51,
-1.48,
-1.36,
-1.11,
-0.7,
-0.44,
-0.37,
-0.3,
-0.23,
-0.22,
0.22,
0.31,
0.39,
0.47,
0.82,
1.1,
1.23,
1.34,
1.42,
1.47]
'''

fit_params, fit_error = fit(exponential, x, y, p0=(1, 1, 1))
errors = np.divide(np.sqrt(np.diag(fit_error))*100, np.abs(fit_params))

plt.title("T1 measurement for heavy mineral oil by inversion-recovery")
plt.xlabel("$\\tau$ (s)")
plt.ylabel("Amplitude (V)")

plt.scatter(x, y, s=20., c="r", marker="x")
plt.plot(np.arange(0.0001, 0.6, 0.001), exponential(np.arange(0.0001, 0.6, 0.001), *fit_params))
plt.legend(["Fit: " + "y={0:.2f}".format(fit_params[0]) + '(1 - E^(-x/' + "{0:.2f}".format(1/fit_params[1]) + ")) + " + "{0:.2f}".format(fit_params[2]), "Raw data"])
plt.savefig("T1_heavy_oil.png")

with open("T1_heavy_oil.txt", 'w') as file:

	file.write("inversion-recovery T1 measurement for heavy mineral oil.\n")
	file.write("Model: " + "{0:.2f}".format(fit_params[0]) + '(1 - E^(-x/' + "{0:.2f}".format(1/fit_params[1]) + ")) + " + "{0:.2f}".format(fit_params[2]) + '\n')
	file.write("Percent error from Std Dev (in order of appearance in model): " + str(errors[0]) + ","+ str(errors[1]) + "," + str(errors[2]) + "\n")





