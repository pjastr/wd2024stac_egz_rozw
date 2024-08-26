import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('sprzedaz23.xlsx')
products = data['Produkt'].unique()
apple = data[data['Produkt'] == 'Jabłka']
pear = data[data['Produkt'] == 'Gruszki']
apricot = data[data['Produkt'] == 'Morele']
x = apple['Rok']
plt.barh(x-0.25, apple['Sprzedaż'], label='Jabłka', height=0.25)
plt.barh(x, pear['Sprzedaż'], label='Gruszki', height=0.25)
plt.barh(x+0.25, apricot['Sprzedaż'], label='Morele', height=0.25)
plt.yticks(x)
plt.title('Sprzedaż owoców w latach 2015-2027')
plt.grid(True)
plt.xlabel('Sprzedaż')
plt.ylabel('Rok')
plt.legend(loc='right')
plt.annotate('26.08.2024', xy=(1700, 2017.2))
plt.tight_layout()
plt.savefig('zad2.pdf')
plt.show()