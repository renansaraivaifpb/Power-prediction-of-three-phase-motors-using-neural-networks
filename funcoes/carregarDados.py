import os  
# arquivo jsonToDateFrame.py
from jsonToDateFrame import jsonToDataFrame

def carregar_dados(pasta):
    dados_list = []
    classePotencia = []
    nomeArquivo = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            nomeArquivo.append(arquivo)
            dados = jsonToDataFrame(os.path.join(diretorio, arquivo))
            dados_list.append(dados)
            classePotencia.append(str(arquivo)[0])
    return dados_list, classePotencia, nomeArquivo