def salvarAmplitudeCSV(amplitude_list_):
    import csv
# Abre o arquivo em modo de escrita
    with open('arquivo.csv', mode='w', newline='') as arquivo:
        # Cria um objeto de escrita de CSV
        escritor = csv.writer(arquivo)
        # Escreve os cabeçalhos no arquivo CSV
        escritor.writerow(['amplitude_X', 'amplitude_Y', 'amplitudeZ'])

        # Para cada linha da lista de dados
        for linha in amplitude_list_:
            # Adiciona o cabeçalho à linha e escreve a linha no arquivo CSV
            escritor.writerow(linha)