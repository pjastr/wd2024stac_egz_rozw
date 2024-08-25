import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('kina12.xlsx')
rok2015 = data[data['Rok'] == 2015]
widownia = rok2015[rok2015['Wykaz'] == 'miejsca na widowni']
colors = ['steelblue', 'darkgreen', 'orange']
labels = widownia['Gestor']
plt.pie(widownia['Wartosc'], colors=colors, startangle = 30, counterclock=True,
        autopct='%1.2f%%', explode=(0.1, 0, 0), labels=labels)
plt.title('Udział miejsc na widowni w kinach w 2015 roku')
plt.annotate('25.08.2024', xy=(-1, 1))
plt.axis('equal')
plt.tight_layout()
plt.savefig('zad2.eps')
plt.show()