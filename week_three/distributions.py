import matplotlib.pyplot as plt
import numpy as np

mean, SD = 9000, 1000
samples = np.random.normal(mean, SD, 1000)

mean2, SD2 = 9000, 1000/np.sqrt(15)
samples2 = np.random.normal(mean2, SD2, 1000)

fig = plt.figure()

plt.subplot(2, 1, 1)
count, bins, ignored = plt.hist(samples, 30, density=True)
plt.plot(bins, 1/(SD * np.sqrt(2 * np.pi)) * 
	np.exp( - (bins - mean)**2 / (2 * SD**2) ),
          linewidth=2, color='r')
plt.title('Population')

plt.subplot(2, 1, 2)
count2, bins2, ignored2 = plt.hist(samples2, 30, density=True)
plt.plot(bins2, 1/(SD2 * np.sqrt(2 * np.pi)) * 
	np.exp( - (bins2 - mean2)**2 / (2 * SD2**2) ),
          linewidth=2, color='r')
plt.xlim(min(samples), max(samples))
plt.ylim(min(count), max(count))

plt.title('Sample')

plt.show()
