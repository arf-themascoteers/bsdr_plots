import numpy as np
import matplotlib.pyplot as plt

v1 = plt.cm.jet(np.linspace(0, 1, 20))[:, :3]
v2 = np.random.rand(20, 1).repeat(3, axis=1)
v3 = v1 * v2

plt.figure(figsize=(2, 10))
for i, color in enumerate(v2):
    plt.fill_between([0, 1], i, i + 1, color=color)
plt.axis('off')
plt.margins(0, 0)
plt.savefig('plot_v2.png', bbox_inches='tight', pad_inches=0)
plt.close()

plt.figure(figsize=(2, 10))
for i, color in enumerate(v1):
    plt.fill_between([0, 1], i, i + 1, color=color)
plt.axis('off')
plt.margins(0, 0)
plt.savefig('plot_v1.png', bbox_inches='tight', pad_inches=0)
plt.close()

plt.figure(figsize=(2, 10))
for i, color in enumerate(v3):
    plt.fill_between([0, 1], i, i + 1, color=color)
plt.axis('off')
plt.margins(0, 0)
plt.savefig('plot_v3.png', bbox_inches='tight', pad_inches=0)
plt.close()
