import numpy as np
import matplotlib.pyplot as plt
import random

def drawHist(x, numbins, rep, minx=0, maxx=1):
    # the histogram of the data
    n, bins, patches = plt.hist(x, numbins, facecolor='green', alpha=0.5)

    plt.xlabel('X')
    plt.ylabel('Freq')
    plt.xlim(minx, maxx)
    plt.title(r'Histogram')

    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)
    plt.savefig('fig' + str(rep) + '.pdf')
    plt.close()

def samp(x, n=20):
    temp_sum = 0.0
    for i in range(n):
        temp_sum += random.choice(x)
    return temp_sum / n

num_bins = 10

# example data
x = np.random.rand(10000)

rep = 1
new_sample = []
for i in range(10):
    new_sample.append(samp(x))
drawHist(new_sample, num_bins, rep)

rep += 1
new_sample = []
for i in range(100):
    new_sample.append(samp(x))
drawHist(new_sample, num_bins, rep)

rep += 1
new_sample = []
for i in range(1000):
    new_sample.append(samp(x))
drawHist(new_sample, num_bins, rep)

rep += 1
new_sample = []
for i in range(10000):
    new_sample.append(samp(x))
drawHist(new_sample, num_bins, rep)

x = np.random.poisson(5, 10000)

rep += 1
new_sample = []
for i in range(10):
    new_sample.append(samp(x))
drawHist(new_sample, num_bins, rep, 3, 7)

rep += 1
new_sample = []
for i in range(100):
    new_sample.append(samp(x))
drawHist(new_sample, num_bins, rep, 3, 7)

rep += 1
new_sample = []
for i in range(1000):
    new_sample.append(samp(x))
drawHist(new_sample, num_bins, rep, 3, 7)

rep += 1
new_sample = []
for i in range(10000):
    new_sample.append(samp(x))
drawHist(new_sample, num_bins, rep, 3, 7)
