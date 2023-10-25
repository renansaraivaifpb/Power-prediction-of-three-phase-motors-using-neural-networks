import pandas as pd 
import scipy.stats
def calculateVariance(windowSize, dados_):
    dados_['variancia_accX'] = dados_['mediaMovel_accX'].rolling(windowSize).var()
    dados_['variancia_accY'] = dados_['mediaMovel_accY'].rolling(windowSize).var()
    dados_['variancia_accZ'] = dados_['mediaMovel_accZ'].rolling(windowSize).var()
    return dados_
