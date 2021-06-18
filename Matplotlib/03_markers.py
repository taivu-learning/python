import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

#
f1 = plt.figure("figure 1")
plt.plot(ypoints, 'o:b')
plt.xlabel("X1")
plt.ylabel("Y1")
f1.show()

#
f2 = plt.figure("figure 2")
# ms = MarkerShape, mec = MarkerEdgeColor, mfc = MarkerFaceColor, ls = linestyle
# dotted = :
plt.plot(ypoints, marker='H', ms=10, mec='y',
         mfc='r', ls='dotted', color='hotpink', lw=3)
plt.xlabel("X2")
plt.ylabel("Y2")
f2.show()

#
input()
