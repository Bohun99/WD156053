#ZADANIE 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

dane = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(dane)
print(df)

group = df.groupby(['Rok']).agg({"Liczba":["sum"]})
print(group)
wykres = group.plot()
wykres.legend()
plt.show()

#ZADANIE 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

dane = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(dane)
print(df)

group = df.groupby(["Plec"]).agg({"Liczba":["sum"]})
print(group)
wykres = group.plot.bar()
wykres.legend()
wykres.set_ylabel("Liczba urodzen")
wykres.set_xlabel("Plec")
plt.show()

#ZADANIE 3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

dane = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(dane)
print(df)

df_5lat = df[(df["Rok"] <= 2017) & (df["Rok"] >= 2013)]

group = df_5lat.groupby(["Plec"]).agg({"Liczba": ["sum"]})
print(group)

wykres = group.plot.pie(subplots=True, autopct="%.2f %%")
plt.title("Ilosc dziewczyn i chlopcow urodzonych miedzy 2013-17")
plt.show()
