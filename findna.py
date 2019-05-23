import pandas as pd
import numpy as np

df1 = pd.read_csv('C:/Users/Utilisateur/Desktop/roster.csv')
df2 = pd.read_csv('C:/Users/Utilisateur/Desktop/roster2.csv')


df[df.isna().any(axis=1)] # Retourne les lignes du df contenant au moins 1 NaN


lst_df =  [df1, df2]
dic_df = {1 : df1, 2 : df2}


# Pour chaque df dans la liste, imprime les lignes contenant au moins 1 NaN
for df in lst_df:
	nan_rows = df[df.isna().any(axis=1)]
	idx = lst_df.index(df)
	print("Lignes contenant des NaN dans le df : '",idx,"'")
	print(nan_rows)
	
idx = lst_df.index(df1)




dic_df = {1 : df1, 2 : df2}

dic_df.keys()[dic_df.values().index(2)]
(list(dic_df.keys())[list(dic_df.values()).index(2)])


search_df = df1
for key, df in dic_df.items():
    if key == search_df:
        print(df)


