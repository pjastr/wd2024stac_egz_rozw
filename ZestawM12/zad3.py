import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('edukacja12.csv', sep=';', decimal=',')
data2 = pd.wide_to_long(data, stubnames=['Matematyka', 'Polski', 'Angielski', 'Biologia', 'Historia'], i='Miasto', j='Rok', sep='_')
data2 = data2.reset_index()
data3 = data2.melt(id_vars=['Miasto', 'Rok'], var_name='Przedmiot', value_name='Wynik')
przedmioty = data3['Przedmiot'].unique()
matematyka = data3[data3['Przedmiot'] == 'Matematyka']
polski = data3[data3['Przedmiot'] == 'Polski']
angielski = data3[data3['Przedmiot'] == 'Angielski']
biologia = data3[data3['Przedmiot'] == 'Biologia']
historia = data3[data3['Przedmiot'] == 'Historia']
miasta = historia['Miasto'].unique()
olsztyn = historia[historia['Miasto'] == 'Olsztyn']
gdansk = historia[historia['Miasto'] == 'Gdańsk']
torun = historia[historia['Miasto'] == 'Toruń']
plt.bar(olsztyn['Rok']-0.25, olsztyn['Wynik'], label='Olsztyn', width=0.25)
plt.bar(gdansk['Rok'], gdansk['Wynik'], label='Gdańsk', width=0.25)
plt.bar(torun['Rok']+0.25, torun['Wynik'], label='Toruń', width=0.25)
plt.grid(True)
plt.legend()
plt.xticks(olsztyn['Rok'])
plt.yticks(np.arange(0, 5))
plt.title('Dane dot. historii w poszczególnych miastach')
plt.xlabel('Rok')
plt.ylabel('Wynik')
plt.savefig('zad3.webp')
plt.show()