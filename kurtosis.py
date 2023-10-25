import pandas as pd 
import scipy.stats
def calculateKurtosis(windowSize, dados_):
    s = pd.DataFrame(dados_).rolling(windowSize).kurt()
    s = s.rename(columns={'mediaMovel_accX': 'curtose_accX', 'mediaMovel_accY': 'curtose_accY', 'mediaMovel_accZ': 'curtose_accZ'})
    return s
