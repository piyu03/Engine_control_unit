#!/usr/bin/env python

import numpy as np
from numpy import genfromtxt

from matplotlib import pyplot as plt

#newdata = pd.read_csv('graph.csv')
newdata = genfromtxt('graph.csv', delimiter=',')

pos = newdata[:,0]


fig, ax = plt.subplots()
fig.set_size_inches(11.69, 8.27)

ax.plot(pos, newdata[:,1], label="Reading 1")
ax.plot(pos, newdata[:,2], label="Reading 2")
ax.plot(pos, newdata[:,3], label="Reading 3")
ax.plot(pos, newdata[:,4], label="Reading 4") # marker= 'x'

ax.fill_between(pos, 0, newdata[:,1], alpha="0.1")
ax.fill_between(pos, 0, newdata[:,2], alpha="0.1")
ax.fill_between(pos, 0, newdata[:,3], alpha="0.1")
ax.fill_between(pos, 0, newdata[:,4], alpha="0.1")

ax.text(3.1, 770, "Controllable region", fontsize=11)
ax.text(4.56, 770, "Un - Controllable region", fontsize=11)

plt.axvline(x=4.5, linestyle='--', color="r")
#ax.fill_between(np.arange(0, 4.50), 0, 600, alpha="0.4")
#ax.fill_between(, 0, 1, where=newdata[:,1] < 500, facecolor='red', alpha=0.5)

ax.grid()

#plt.legend()

plt.xlabel('Throttle Position (mm)')
plt.ylabel('Engine speed (RPM)')

plt.title("IC Engine Throttle Response")
plt.savefig("test.png")

plt.show()

#ax.set_xlim(-2.1,2.1)
