import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

def calculeMediaMovel(windowSize, dados_):
    dados1 = dados_['accX'].to_frame()
    dados1['accX'] = dados1['accX'].rolling(windowSize).mean()

    dados2 = dados_['accY'].to_frame()
    dados2['accY'] = dados2['accY'].rolling(windowSize).mean()

    dados3 = dados_['accZ'].to_frame()
    dados3['accZ'] = dados3['accZ'].rolling(windowSize).mean()

    df1 = pd.merge(dados1['accX'], dados2['accY'], right_index = True,
               left_index = True)

    df2 = pd.merge(df1, dados3['accZ'], right_index = True,
               left_index = True)
    df2 = df2.rename(columns={'accX': 'mediaMovel_accX', 'accY': 'mediaMovel_accY', 'accZ': 'mediaMovel_accZ'})
    return df2
