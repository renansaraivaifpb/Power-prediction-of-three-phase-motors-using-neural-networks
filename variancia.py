import pandas as pd 
import scipy.stats
def calcularVariance(windowSize, dados_):
    s = pd.DataFrame(dados_).rolling(3).var()
    s = s.rename(columns={'mediaMovel_accX': 'variancia_accX', 'mediaMovel_accY': 'variancia_accY', 'mediaMovel_accZ': 'variancia_accZ'})
    return s