import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (5, 4), dpi = 100)
plt.axhline(0, c = "gray", linestyle = "-")
plt.axvline(0, c = "gray", linestyle = "-")

x = np.arange(-2 * np.pi, 2 * np.pi, 0.02)
y = np.sin(x) + 0.5 * np.sin(3 * x)

x_ = 40 * x
y_ = 80 * y

plt.plot(x_, y_)
plt.show()