from scipy.stats import norm
import random
import matplotlib.pyplot as plt
import numpy as np

samples = 10000
change_point = 5000
P = {"x": [], "norm1": [], "norm2": [], "P1": [], "P2": []}
norm0 = norm.rvs(loc=0, scale=1)
norm1 = norm.rvs(loc=10, scale=2)

random_list = []

for i in range(samples):
    if i < change_point:
        rnd_number = random.normalvariate(0, 1)

    else:
        rnd_number = random.normalvariate(10, 1)
    P["x"].append(rnd_number)
    pdf1 = norm.pdf(rnd_number, 0, 1)
    pdf2 = norm.pdf(rnd_number, 10, 1)
    P["norm1"].append(pdf1)
    P["norm2"].append(pdf2)
    P["P1"].append(0.5 * pdf1 / (0.5 * (pdf1 + pdf2)))
    P["P2"].append(0.5 * pdf2 / (0.5 * (pdf1 + pdf2)))
plt.plot(-np.log10((P["norm1"])))
plt.plot(-np.log10(P["norm2"]))
plt.figure(2)
plt.plot(P["x"])
plt.figure(3)
plt.plot(P["P1"])
plt.figure(4)
plt.plot(P["P2"])

plt.show()


