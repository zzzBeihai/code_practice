import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (4, 4), dpi = 100)
plt.axhline(0, color = 'g', linestyle = '-')
plt.axvline(0, color = 'g', linestyle = '-')

plt.xlim(-200, 200)
plt.ylim(-200, 200)

x = np.arange(-np.pi, np.pi, 0.02)
y = 4 * np.cos(x) - np.cos(6 * x)

x_ = x * 30
y_ = y * 30

plt.hlines(y_, 0, x_, colors="red", linewidth=0.8)
plt.show()
