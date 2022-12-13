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
