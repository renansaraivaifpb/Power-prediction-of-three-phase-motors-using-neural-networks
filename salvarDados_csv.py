import os  
import csv
import time

def salvar_csv(dados_):
    '''f = open('dados.csv', 'w', newline='', encoding='utf-8')
    dados_.to_csv('dados.csv')'''
    for i in range(len(dados_)):
        if os.path.exists('dados') == True:
            dados_[i].to_csv('dados/analises/potencia230/out.csv', mode='a', index=False)
        else:
            os.makedirs('dados/analises/potencia230', exist_ok=True)  
            dados_[i].to_csv('dados/analises/potencia230/out.csv', index=False, header = True)