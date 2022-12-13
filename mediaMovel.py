import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

def calculeMediaMovel(windowSize, eixo, dados_):
    # usando .to_frame() para converter séries de pandas
    # no dataframe.
    dados = dados_[eixo].to_frame()

    # calculando média móvel simples
    # usando .rolling(window).mean() ,
    # com tamanho da janela = windowSize
    dados[eixo] = dados[eixo].rolling(windowSize).mean()
    dados.plot(figsize=(12, 5))
    sns.lineplot(data = dados) 
    plt.show()
