import numpy as np
import matplotlib.pyplot as plt

colors = plt.cm.jet(np.linspace(0, 1, 20))
plt.figure(figsize=(2, 10))
for i, color in enumerate(colors):
    plt.fill_between([0, 1], i, i+1, color=color)
plt.axis('off')
plt.show()
