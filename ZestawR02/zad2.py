import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("ceny02.xlsx")
jablka = data[data["Rodzaje towarów i usług"] == "jabłka - za 1kg"]
cytryny = data[data["Rodzaje towarów i usług"] == "cytryny - za 1 kg"]
x = np.arange(len(jablka["Miesiące"]))
plt.plot(x, jablka["Wartosc"], label='jabłka', linestyle='-', linewidth=2)
plt.plot(x, cytryny["Wartosc"], label='cytryny', linestyle='--', linewidth=3)
plt.grid()
plt.legend()
plt.annotate('max', xy=(7, 14), xytext=(8, 4),
             arrowprops=dict(facecolor='black'))
plt.xlabel('Miesiące')
plt.ylabel('Cena w zł')
plt.xticks(x, jablka["Miesiące"], rotation=45)
plt.title('Ceny jabłek i cytryn w 2017')
plt.tight_layout()
plt.savefig('zad2.webp')
plt.show()
