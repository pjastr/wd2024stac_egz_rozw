import matplotlib.pyplot as plt

x = [73, 74, 76, 85]
y1 = [40, 59, 39, 38]
y2 = [61, 65, 58, 65]
plt.plot(x, y2, color='violet')
plt.scatter(x, y2, color='blue', marker='x', label='krzyżyki', s=100)
plt.plot(x, y1, color='orange')
plt.scatter(x, y1, color='blue', marker='>', label='trójkąty', s=100)
plt.grid()
plt.title('Wykres punktowy z liniowym - 2 x 4 punkty')
plt.legend()
plt.savefig('zad1.jpg')
plt.show()