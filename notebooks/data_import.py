import pandas as pd
from datetime import datetime
import re

df = pd.read_excel('C:/Users/mpast/Desktop/Tesi-Magistrale/data/A2A/A2A_8.xlsx')

# tolgo la prima riga perchè è quella che contiene il sommario del time range annuale
df = df.iloc[1:]

# creo una colonna di valori booleani che mi indicano se la prima colonna contiene una data 
# oppure il time-range di riferimento
df['Flag Giorno VS TimeRange'] = df['Intervallo tempo'].str.contains(r'[a-zA-Z]', na=False)

pd.set_option('display.max_rows', 100)
print(df.head(100))
