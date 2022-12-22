import numpy as np
def calcularAmplitude(dados_, x):
    '''
     o valor de x é o número de pontos mais altos ou mais baixos que você deseja considerar. 
     Por exemplo, se você quiser calcular a amplitude dos 10 pontos mais altos e mais baixos da 
     lista, basta definir x como 10 
    '''
    df_sorted = dados_.sort_values(by=['accX', 'accY', 'accZ'], ascending=False)
    return np.mean(df_sorted[x:], axis=0) - np.mean(df_sorted[:x], axis=0)
