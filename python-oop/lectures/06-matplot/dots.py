import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 1, figsize=(5, 8))

for idx, ax in enumerate(axes):
    x = np.random.normal(3.5, 2.16, 24)
    y = np.random.normal(3.5, 2.16, 24)
    sizes = np.random.uniform(50, 200, 24)
    for i in range(24):
        ax.plot(x[i], y[i], marker="o", linestyle="None",
                markersize=np.sqrt(sizes[i]),
                color=np.random.uniform(0, 1, 3))

    ax.set_xticks(range(1, 8))
    ax.set_yticks(range(1, 8))
    ax.axis([1, 7, 1, 7])

    ax.set_aspect("equal", "box")

    if idx == 0:
        ax.tick_params(axis="x", top=True, labeltop=True, bottom=False, labelbottom=False)
    else:
        ax.tick_params(axis="x", top=False, labeltop=False, bottom=True, labelbottom=True)
    ax.tick_params(axis="y", left=True, right=True, labelleft=True, labelright=True)

plt.tight_layout()
plt.show()
