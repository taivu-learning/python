import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(200, size=(50))
y = np.random.randint(1000, size=(50))
colors = np.random.randint(50, size=(50))
sizes = 10 * np.random.randint(100, size=(50))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap='nipy_spectral')

plt.colorbar()
plt.suptitle("Combine")

plt.show()
