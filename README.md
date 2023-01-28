# Aplicação Embarcada para detectar alguns parâmetros de Motores de Indução

Este conjunto de códigos fornece funções para trabalhar com dados de acelerômetro, armazenados em arquivos JSON. As principais funções incluem:


A função jsonToDataFrame, que converte um arquivo JSON em um DataFrame do pandas com colunas 'accX', 'accY' e 'accZ'.

A função calcularMediaMovel, que calcula e adiciona as colunas de média móvel para o DataFrame para cada eixo (accX, accY, accZ) com base em um tamanho de janela especificado.

A função calcularCurtose, que calcula e adiciona as colunas de curtose para o DataFrame para cada eixo (accX, accY, accZ) com base em um tamanho de janela especificado.

A função carregar_dados, que busca todos os arquivos JSON em uma pasta especificada e os carrega em um DataFrame utilizando a função jsonToDataFrame. Ele também cria uma lista de classes de potência e nomes de arquivo correspondentes para cada conjunto de dados.


Em resumo, esses códigos fornecem ferramentas para carregar, processar e trabalhar com dados de acelerômetro em formato JSON, incluindo cálculos de média móvel e curtose.

