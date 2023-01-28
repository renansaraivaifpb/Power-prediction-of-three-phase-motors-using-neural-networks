import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

def calculeMediaMovel(windowSize, dados_):
    dados_['mediaMovel_accX'] = dados_['accX'].rolling(windowSize).mean()
    dados_['mediaMovel_accY'] = dados_['accY'].rolling(windowSize).mean()
    dados_['mediaMovel_accZ'] = dados_['accZ'].rolling(windowSize).mean()
    return dados_
