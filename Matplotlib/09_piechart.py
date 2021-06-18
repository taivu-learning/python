import matplotlib.pyplot as plt
import numpy as np

#
y1 = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

f1 = plt.figure("Fruits")
plt.pie(y1, labels=mylabels)
f1.show()

#
y2 = np.array([35, 25, 25, 15])
mylabels2 = ["Apples", "Bananas", "Cherries", "Dates"]

f2 = plt.figure("Fruits 2")
plt.pie(y2, labels=mylabels2, startangle=90)
f2.show()

#
y3 = np.array([35, 25, 25, 15])
mylabels3 = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

f3 = plt.figure("Fruits 3")
plt.pie(y3, labels=mylabels3, startangle=90, explode=myexplode, shadow=True)
plt.legend(title="Four fruit")
f3.show()

#
input()
