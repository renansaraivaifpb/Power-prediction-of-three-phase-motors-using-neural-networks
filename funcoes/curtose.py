import pandas as pd 
def calcularCurtose(windowSize, dados_):
    ''' Calculate Kurtosis '''
    dados_['accX Kurtosis'] = dados_['accX'].rolling(windowSize).kurt()
    dados_['accY Kurtosis'] = dados_['accY'].rolling(windowSize).kurt()
    dados_['accZ Kurtosis'] = dados_['accZ'].rolling(windowSize).kurt()
    
    return dados_
