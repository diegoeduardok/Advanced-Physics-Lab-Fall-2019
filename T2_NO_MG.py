import numpy as np 
from scipy.optimize import curve_fit as fit 
from matplotlib import pyplot as plt

def exponential(x, c0, tau, c1):
	return c0*np.exp(-x*tau) + c1
'''
x =[0.002,
	0.006,
	0.018,
	0.032,
	0.054,
	0.064,
	0.074,
	0.084,
	0.094,
	0.104,
	0.114]

y =[6.42,
	5.77,
	4.27,
	3,
	1.8,
	1.48,
	1.23,
	1.03,
	0.867,
	0.746,
	0.63]
'''

x = [0.002,
0.006,
0.01,
0.02,
0.04,
0.06,
0.07,
0.1,
0.12,
0.14,
0.16
]

y = [7.84,
7.73,
7.46,
7.27,
6.15,
4.71,
3.76,
1.66,
0.98,
0.56,
0.35
]

fit_params, fit_error = fit(exponential, x, y, p0=(6.5, 20, 1))
errors = np.divide(np.sqrt(np.diag(fit_error))*100, fit_params)

plt.title("Spin-echo T2 measurement for distilled water")
plt.xlabel("$2 \\tau$ (s)")
plt.ylabel("Amplitude (V)")

plt.scatter(x, y, marker="x", c="r", s=20.)
plt.plot(np.arange(0, 0.16, 0.0001), exponential(np.arange(0, 0.16, 0.0001), *fit_params))
plt.legend(["Fit: " + "y={0:.2f}".format(fit_params[0]) + '*E^(-x/' + "{0:.2f}".format(1/fit_params[1]) + ") + " + "{0:.2f}".format(fit_params[2]),
			"Raw data"])

plt.savefig("T2_distilled_water_no_MG.png")

with open("T2_distilled_water_no_MG.txt", 'w') as file:

	file.write("Spin-echo measurement for distilled water.\n")
	file.write("Model: " + "{0:.2f}".format(fit_params[0]) + '*E^(-x/' + "{0:.2f}".format(1/fit_params[1]) + ") + " + "{0:.2f}".format(fit_params[2]) + '\n')
	file.write("Percent error from Std Dev (in order of appearance in model): " + str(errors[0]) + ","+ str(errors[1]) + "," + str(errors[2]) + "\n")




