import pandas as pd 
from scipy.stats import skew
# Skewness (asymmetry) of a data distribution
def calcularSkewness(dados_):
    # calculate the skewness of acceleration data
    dados_['accX Skewness'] = skew(dados_['accX'])
    dados_['accY Skewness'] = skew(dados_['accY'])
    dados_['accZ Skewness'] = skew(dados_['accZ'])
    return dados_
