import numpy as np
import matplotlib.pyplot as plt

v1 = plt.cm.jet(np.linspace(0, 1, 20))[:, :3]
white_slots = np.random.choice(20, 12, replace=False)
v1[white_slots] = [1, 1, 1]

plt.figure(figsize=(2, 10))
for i, color in enumerate(v1):
    plt.fill_between([0, 1], i, i + 1, color=color)
plt.axis('off')
plt.margins(0, 0)
plt.savefig('plot_jet_with_white.png', bbox_inches='tight', pad_inches=0)
plt.close()
