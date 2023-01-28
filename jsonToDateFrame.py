import json
import pandas as pd

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
