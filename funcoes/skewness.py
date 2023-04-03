import pandas as pd 
from scipy.stats import skew
# Skewness (assimetria) de uma distribuição de dados
def calcularSkewness(dados_):
    # calcular a Skewness dos dados de aceleração
    dados_['accX Skewness'] = skew(dados_['accX'])
    dados_['accY Skewness'] = skew(dados_['accY'])
    dados_['accZ Skewness'] = skew(dados_['accZ'])
    return dados_