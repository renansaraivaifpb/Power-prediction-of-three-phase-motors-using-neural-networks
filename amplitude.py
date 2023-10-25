import numpy as np
def calculateAmplitude(dados_, x):
    '''
     the value of x is the number of highest or lowest points you want to consider.
      For example, if you want to calculate the amplitude of the 10 highest and lowest points in the
      list, just set x to 10 
    '''
    df_sorted = dados_.sort_values(by=['accX', 'accY', 'accZ'], ascending=False)
    return np.mean(df_sorted[x:], axis=0) - np.mean(df_sorted[:x], axis=0)
