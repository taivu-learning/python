import matplotlib.pyplot as plt
import numpy as np

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}

#
y1points = np.array([3, 8, 1, 10])
y2points = np.array([2, 9, 3, 7])

f1 = plt.figure("Multi lines 1")
plt.title("Car sale Data", fontdict=font1)
plt.plot(y1points)
plt.plot(y2points)
f1.show()

#
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
f2 = plt.figure("Multi lines 2")
plt.title("Sports Watch Data", fontdict=font1)
plt.plot(x1, y1, x2, y2)
f2.show()

#
input()
