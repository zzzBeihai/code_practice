import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize = (4.8, 4.8), dpi = 100)
plt.axhline(0, c = "g", linestyle = "-")
plt.axvline(0, c = "g", linestyle = "-")
x = np.arange(-2 * np.pi, 2 * np.pi, 0.03)
y = 3 * np.sin(x) + np.sin(3 * x)
x_ = x * 25
y_ = y * 25
plt.vlines(x_, 0, y_, color = "orange", linewidth = 0.8)
plt.plot(x_, y_)
plt.show()
