import pandas as pd
import numpy as np



# bibliotecas que transformar os dados brutos nas features desejadas
from funcoes.curtose import calcularCurtose
from funcoes.skewness import calcularSkewness
from funcoes.rms import calcularRMS
from funcoes.spectralPower import calcularSpectralPower

from funcoes.carregarDados import carregar_dados


# essa variável serve para ler e salvar o tipo de Set, em csv
conjunto = 'testing'
pasta = conjunto+'/'
# Load data
dados_list, classePotencia, nomeArquivo = carregar_dados(pasta)


curtose_list = [calcularCurtose(25,dados_list[i]) for i in range(len(dados_list))]

skewness_list = [calcularSkewness(curtose_list[i]) for i in range(len(dados_list))]

rms = [calcularRMS(skewness_list[i]) for i in range(len(dados_list))]

'''spectralPower = [calcularSpectralPower(rms[i], 62.5) for i in range(len(dados_list))]
'''
print(rms[0])
print(calcularSpectralPower(rms[0], 62.5))
