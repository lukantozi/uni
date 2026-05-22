import matplotlib.pyplot as plt

x = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
y = [22.5, 17, 9, 8, 7, 6]
bar_colors = ["red", "black", "green", "blue", "yellow", "cyan"]

plt.bar(x,y, color=bar_colors, zorder=2)
plt.xticks(list(range(len(y))), x)
plt.minorticks_on()

plt.grid(which = "major", linestyle = "-", linewidth="0.5", color="red", zorder=1)
plt.grid(which = "minor", linestyle = ":", linewidth="0.5", color="black")
plt.show()
