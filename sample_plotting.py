#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 13:51:19 2018

@author: ziaulchoudhury
works cited: mathplotlib examples available online 
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d


#---Basic plot line---#
plt.plot([1,2,3,4])
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.show()

#---Basic plot with dots---#
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.show()

#---Basic plot with 3 types---#
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


#-----Customize Plot-----#
plt.style.use('ggplot')
data = np.random.randn(50)

# Plot with dark background
with plt.style.context(('dark_background')):
    plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'w-o') #white dots
plt.show()

# Plot with gray background simpler version
mpl.rcParams['lines.linewidth'] = 4
mpl.rcParams['lines.color'] = 'r'
plt.plot(data)
plt.show()

#------Individual plots and subplot------#
np.random.seed(99999)
data = np.random.randn(2, 100)

plt.hist(data[0])
plt.show()

plt.scatter(data[0], data[1])
plt.show()

plt.plot(data[0], data[1])
plt.show()

plt.hist2d(data[0], data[1])
plt.show()

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])
plt.show()




#------Plots with logarithmic axes.-------#
# Data for plotting
t = np.arange(0.01, 20.0, 0.01)

# Create figure
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

# log y axis
ax1.semilogy(t, np.exp(-t / 5.0))
ax1.set(title='semilogy')
ax1.grid()

# log x axis
ax2.semilogx(t, np.sin(2 * np.pi * t))
ax2.set(title='semilogx')
ax2.grid()

# log x and y axis
ax3.loglog(t, 20 * np.exp(-t / 10.0), basex=2)
ax3.set(title='loglog base 2 on x')
ax3.grid()

# With errorbars: clip non-positive values
# Use new data for plotting
x = 10.0**np.linspace(0.0, 2.0, 20)
y = x**2.0

ax4.set_xscale("log", nonposx='clip')
ax4.set_yscale("log", nonposy='clip')
ax4.set(title='Errorbars go negative')
ax4.errorbar(x, y, xerr=0.1 * x, yerr=5.0 + 0.75 * y)
# ylim must be set after errorbar to allow errorbar to autoscale limits
ax4.set_ylim(ymin=0.1)

fig.tight_layout()
plt.show()

#-----Plots using legend-----#
# Make some fake data.
a = b = np.arange(0, 3, .02)
c = np.exp(a)
d = c[::-1]

# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length', color='blue')
ax.plot(a, d, 'k:', label='Data length', color='green')
ax.plot(a, c + d, 'k', label='Total message length', color='red')

legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#00FFCC')

plt.show()

#-----3D plot-----#

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grab some test data.
X, Y, Z = axes3d.get_test_data(0.03)

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=15, cstride=15)

plt.show()

