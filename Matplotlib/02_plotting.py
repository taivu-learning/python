import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# A simple line
x1points = np.array([1, 8])
y1points = np.array([3, 10])
f1 = plt.figure("A simple line")
plt.plot(x1points, y1points)

# Some markers
x2points = np.array([1, 3, 5, 8])
y2points = np.array([4, 8, 5, 10])
f2 = plt.figure("Display as markers")
plt.plot(x2points, y2points, 'o')

# Multiple lines
x3points = np.array([1, 3, 5, 8])
y3points = np.array([4, 8, 5, 10])
f3 = plt.figure("Multiple lines")
plt.plot(x3points, y3points)

# Multiple lines with default x points
y4points = np.array([4, 8, 5, 10])
f4 = plt.figure("Multiple lines with default x points")
plt.plot(y4points)

# Plotting
f1.show()
f2.show()
f3.show()
f4.show()
# plt.show()  // Option 2: Replace all f.show() by this line


# Wait
input()
