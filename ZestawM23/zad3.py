import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('travel23.csv', sep=';')
data2 = data.melt(id_vars='Podróż', value_vars=['Transport', 'Zakwaterowanie', 'Jedzenie', 'Zwiedzanie', 'Inne'],
                  var_name='Kategoria', value_name='Koszt')
wlochy = data2[data2['Podróż'] == 'Włochy']
hiszpania = data2[data2['Podróż'] == 'Hiszpania']
colors = ['lime', 'cyan', 'magenta', 'yellow', 'red']
plt.subplot(1, 2, 1)
plt.pie(wlochy['Koszt'], labels=wlochy['Kategoria'], autopct='%1.1f%%', startangle=80, colors=colors)
plt.title('Włochy')
plt.axis('equal')
plt.subplot(1, 2, 2)
plt.pie(hiszpania['Koszt'], labels=hiszpania['Kategoria'], autopct='%1.1f%%', startangle=80, colors=colors)
plt.title('Hiszpania')
plt.axis('equal')
plt.tight_layout()
plt.savefig('zad3.png')
plt.show()