import numpy as np
import matplotlib.pyplot as plt

colors = np.random.rand(20, 1).repeat(3, axis=1)
plt.figure(figsize=(2, 10))
for i, color in enumerate(colors):
    plt.fill_between([0, 1], i, i + 1, color=color)
plt.axis('off')
plt.savefig('weights.png')
