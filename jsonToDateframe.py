import pandas as pd

# bibliotecas para visualizações
import seaborn as sns
import matplotlib.pyplot as plt

# arquivo carregarDados.py
from carregarDados import carregar_dados

# arquivo mediaMovel.py
from mediaMovel import calculeMediaMovel

# arquivo variancia.py
from variancia import calcularVariance

# arquivo curtose.py
from curtose import calcularCurtose

# arquivo amplitude.py
from amplitude import calcularAmplitude

# arquivo salvarAmplitudeCsv.py
# from salvarAmplitudeCsv import salvarAmplitudeCSV

def visualizarDados(dados):
    ''' Função de plotagem '''
    sns.jointplot(data=dados)
    plt.show()

conjunto = 'testing'
pasta = conjunto+'/'

# Load data
dados_list, classePotencia, nomeArquivo = carregar_dados(pasta)

# numero total de listas
# cada tabela representa um arquivo 
# Calculate moving averages
media_list = [calculeMediaMovel(25, dados_list[i]) for i in range(len(dados_list))]

# Calculate variance
variancia_list = [calcularVariance(25, dados_list[i]) for i in range(len(dados_list))]

# Merge moving averages and variance
df2_list = [pd.merge(media_list[i], variancia_list[i], right_index = True, left_index = True) for i in range(len(dados_list))]


# Calculate kurtosis
curtose_list = [calcularCurtose(25,dados_list[i]) for i in range(len(dados_list))]


# Merge df2 and kurtosis
df3_list = [pd.merge(df2_list[i], curtose_list[i], right_index = True, left_index = True) for i in range(len(dados_list))]


# Calculate amplitude
amplitude_list = [calcularAmplitude(dados_list[i],10) for i in range(len(dados_list))]

df1 = pd.DataFrame(amplitude_list)
df2 = pd.DataFrame(classePotencia, columns=['Y'])

# Mapeando valores da classe de potencia
df2['Y'] = df2['Y'].map({'A': 0.22, 'B': 0.32, 'C': 0.62, 'D': 1.15, 'E': 0.27, 'F': 0.50, 'G': 0.85, 'H': 1.00})

# Concatenando dataframes
conjuntoDados = pd.concat([df1, df2], axis=1, ignore_index=True)

# Renomeando colunas
conjuntoDados.columns = list(df1.columns) + ['Y']

# Salvando em arquivo CSV
conjuntoDados.to_csv(conjunto+'.csv', index=False)
