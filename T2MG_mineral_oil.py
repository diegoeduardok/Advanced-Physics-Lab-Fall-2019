import numpy as np 
from scipy.optimize import curve_fit as fit 
from scipy.signal import find_peaks
from matplotlib import pyplot as plt 

def exponential(x, c0, tau, c1): #Fitting function
	return c0*np.exp(-x*tau) + c1

#Get data and pick relevant points (peaks)
times = []
amplitudes = []

with open("C1t2mgh2ogood00000.txt", 'r') as file:
	for line in file.readlines()[23000::10]: #Drop data points before waveform begins. Downsample by 10.
		time, amplitude = line.split(',')

		times.append(float(time))
		amplitudes.append(float(amplitude))

	times = np.asarray(times)
	amplitudes = np.asarray(amplitudes)

peaks, properties = find_peaks(amplitudes, height=exponential(times, 5.65, 1/0.04, 0.5), distance=1000)


#Fit data. Write data and fit to a file.

fit_params, fit_error = fit(exponential, times[peaks], amplitudes[peaks], p0=(6.5, 20, 1))
errors = np.divide(np.sqrt(np.diag(fit_error))*100, fit_params)

print("Model: " + str(fit_params[0]) + '*E^(-x/' + str(1/fit_params[1]) + ") + " + str(fit_params[2]))

plt.title("MG spin-echo measurement for heavy mineral oil")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (V)")

plt.plot(times, amplitudes)
plt.scatter(times[peaks], amplitudes[peaks], s=20, marker="x", c="r")
plt.plot(np.arange(0, 0.2, 0.001), exponential(np.arange(0, 0.2, 0.001), *fit_params))
plt.legend(["Raw data", 
			"Fit: " + "y={0:.2f}".format(fit_params[0]) + '*E^(-x/' + "{0:.2f}".format(1/fit_params[1]) + ") + " + "{0:.2f}".format(fit_params[2]),  
			"Filtered peaks"])

plt.savefig("figure_1.png")

with open("T2_heavy_oil_MG.txt", 'w') as file:

	file.write("MG spin-echo measurement for heavy mineral oil.\n")
	file.write("Model: " + "{0:.2f}".format(fit_params[0]) + '*E^(-x/' + "{0:.2f}".format(1/fit_params[1]) + ") + " + "{0:.2f}".format(fit_params[2]) + '\n')
	file.write("Percent error from Std Dev (in order of appearance in model): " + str(errors[0]) + ","+ str(errors[1]) + "," + str(errors[2]) + "\n")
	file.write("time(s),amplitude(V)\n")

	for peak in peaks:
		file.write(str(times[peak]) + "," + str(amplitudes[peak]))
		file.write('\n')
