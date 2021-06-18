import matplotlib.pyplot as plt
import numpy as np

# bar 1
x1 = np.array(["A", "B", "C", "D"])
y1 = np.array([3, 8, 1, 10])

f1 = plt.figure("First bar")
plt.bar(x1, y1, color="blue", width=0.3)
plt.title("Virtical bar")
f1.show()

# bar 2
x2 = np.array(["A", "B", "C", "D"])
y2 = np.array([3, 8, 1, 10])

f2 = plt.figure("Second bar")
plt.barh(x2, y2, color="red", height=0.5)
plt.title("Horizontal bar")
f2.show()

#
input()
