
# importar as bibliotecas necessárias
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# bibliotecas para conversão
import pandas as pd

# BASE DE DADOS ACELOMETRO

# treinamento
X_train = pd.read_csv('training.csv', sep =',', usecols=lambda column: column in ['accX','accY','accZ']) # matriz de amostras de aceleração x, y e z
y_train = pd.read_csv('training.csv', sep =',', usecols=lambda column: column in ['Y'])
# como a array é bidimencional e que a função svr aceita apenas uni então deve fazer essa conversão
y_train = y_train.values.ravel()
# teste
X_test = pd.read_csv('testing.csv', sep =',', usecols=lambda column: column in ['accX','accY','accZ'])
y_test = pd.read_csv('testing.csv', sep =',', usecols=lambda column: column in ['Y'])
y_test = y_test.values.ravel()

# Criando o objeto SVR
svr = SVR(kernel='linear', C=1.0, epsilon=0.2)

# Treinando o modelo
svr.fit(X_train, y_train)

# Fazendo previsões
y_pred = svr.predict(X_test)

# Calculando o erro médio quadrático
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)
