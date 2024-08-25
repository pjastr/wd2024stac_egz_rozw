import numpy as np
import matplotlib.pyplot as plt

blue = np.array([29, 19, 38, 17, 18])
green = np.array([13, 20, 11, 19, 21])
pink = np.array([15, 22, 9, 19, 24])
x = np.arange(2010,2015)
plt.bar(x, blue, color='tab:blue', label='A')
plt.bar(x, green, color='darkgreen', label='B', bottom=blue)
plt.bar(x, pink, color='pink', label='C', bottom=blue+green)
plt.legend()
plt.title('Słupki potrójne')
plt.ylim(0,80)
plt.yticks(np.arange(0, 81, 10), color='orange')
plt.xticks(x, color='steelblue')
plt.savefig('zad1.jpg')
plt.show()