import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E']
sizes1 = [27.2, 8.8, 28.1, 21.1, 14.9]
sizes2 = [25.7, 21.2, 13.4, 12.8, 26.8]
colors1 = ['gray', 'linen', 'lightyellow', 'lightcoral', 'yellowgreen']
colors2 = ['cyan', 'darkorange', 'khaki', 'green', 'red']
explode1 = (0, 0.1, 0, 0, 0)
plt.subplot(2, 1, 1)
plt.pie(sizes1, labels=labels, colors=colors1, autopct='%1.1f%%', shadow=True, startangle=10, explode=explode1)
plt.title('Tytuł 1')
plt.subplot(2, 1, 2)
plt.pie(sizes2, labels=labels, colors=colors2, autopct='%1.1f%%', shadow=True, startangle=10, explode=explode1)
plt.title('Tytuł 2')
plt.tight_layout()
plt.savefig('zad1.svg')
plt.show()
