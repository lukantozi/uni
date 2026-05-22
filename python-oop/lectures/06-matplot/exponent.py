import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, num=100)
y = [(4 + x1**2) for x1 in x]
y1 = [(1 + 2*x1) for x1 in x]
y2 = np.add(y, y1) / 2

plt.yticks(list(range(1, 23, 3)))
plt.xticks(list(range(1, 8)))
plt.axis([0, 8, 0, 23])

plt.plot(x,y2, color="red", label="f(x)")
plt.grid(True, color = "red", linewidth = 1.5, linestyle=":")

plt.title("Important chart with font size 24", fontsize=24)
plt.xlabel("This is xlabel with math symbol a > b * xi")
plt.ylabel("This is ylabel")
plt.legend(loc="center left", fontsize="x-large", title_fontsize="x-large")
plt.text(5.2, 6, "boxed oblique text\nin position 5.2, 6", fontsize=15, bbox=dict(facecolor="red", alpha=0.5))

plt.fill_between(x, y, y1)
plt.show()
