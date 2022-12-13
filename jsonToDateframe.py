# bibliotecas para conversão
import pandas as pd
import json

# bibliotecas para visualizações
import seaborn as sns
import matplotlib.pyplot as plt


def visualizarDados(dados):
    ''' Função de plotagem '''
    sns.jointplot(data=dados)
    plt.show()


def jsonToDataFrame(address_file):
    ''' Função que retorna dado estruturado em DataFrame '''
    with open(address_file) as jsonfile:
        data = json.load(jsonfile)
    # chave e valor
    lista = data['payload']['values']
    # transforma a lista em uma variavel do tipo dataframe com as seguintes,
    # colunas: 'accX','accY','accZ'
    df = pd.DataFrame (lista, columns = ['accX','accY','accZ'])
    return df


## comandos para selecionar o arquivo
address = input("Digite local de arquivo: ")
dados = jsonToDataFrame(address)
# visualizarDados(dados)
# POTENCIA 230W
# Training/potencia-230W/A.3jjeujup.ingestion-5b88b9545f-7r6tj.json
# POTENCIA 320W
# Training/potencia-320W/B.3jjfahvd.ingestion-5b88b9545f-ltdhd.json
# POTENCIA 620W
# Training/potencia-620W/C.3jjfl9vo.ingestion-5b88b9545f-ltdhd.json
# POTENCIA 1100W
# Training/potencia-1100W/D.3jjg0o89.ingestion-5b88b9545f-ltdhd.json

def mediaMovel(windowSize, eixo, dados_):
    # atualizando nosso dataFrame para ter apenas
    # uma coluna 'Fechar' como resto todas as colunas
    # são inúteis para nós no momento
    # usando .to_frame() para converter séries de pandas
    # no dataframe.
    dados = dados_[eixo].to_frame()

    # calculando média móvel simples
    # usando .rolling(window).mean() ,
    # com tamanho da janela = 30
    dados[eixo] = dados[eixo].rolling(windowSize).mean()
    dados[[eixo]].plot(figsize=(16, 8))
    sns.lineplot(data = dados) 
    plt.show()

plotarMediaMovel = int(input("Digite o tamanho da janela: "))
# separe os eixos com espaços
verificarEixo = input("Digite o eixo(s) que deseja verificar: ")
# quebrar a string que contem espaços
# eixos = verificarEixo.split()
mediaMovel(plotarMediaMovel, verificarEixo, dados)

