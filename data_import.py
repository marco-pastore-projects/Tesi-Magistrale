import pandas as pd

df = pd.read_excel('C:/Users/mpast/Desktop/Tesi-Magistrale/A2A_8.xlsx')

print(df['Intervallo tempo'].str.contains('JAN').index)

# print(df.head())


