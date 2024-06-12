import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("samochody02.xlsx", header=None).T
data.columns = ["Rodzaj", "Rok", "Wartość"]
data["Rok"] = data["Rok"].astype(int)
data["Wartość"] = data["Wartość"].astype(int)
r2017 = data[data["Rok"] == 2017]
r2018 = data[data["Rok"] == 2018]
x = np.arange(len(r2017["Rodzaj"]))
plt.barh(x, r2017["Wartość"], label='2017', height=0.33)
plt.barh(x + 0.33, r2018["Wartość"], label='2018', height=0.33)
plt.yticks(x + 0.33 / 2, r2017["Rodzaj"])
plt.xticks([0, 10000000, 20000000], ['0', '10 mln', '20 mln'])
plt.legend()
plt.title('Dane samochodów w 2017 i 2018')
plt.tight_layout()
plt.savefig('zad3.png')
plt.show()
