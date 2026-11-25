import matplotlib.pyplot as plt

xs, ys = [], []
x = -5
while x < 5:
    xs.append(x)
    ys.append(x * x)
    x += 0.1
plt.plot(xs, ys)
plt.show()