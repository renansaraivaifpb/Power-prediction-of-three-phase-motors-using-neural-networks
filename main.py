import pandas as pd

# libraries for visualization
import seaborn as sns
import matplotlib.pyplot as plt

# file loadData.py
from loadData import load_Data

# file moving_average.py
from moving_average import calculateMoving_average

# file variance.py
from variance import calculateVariance

# file kurtosis.py
from kurtosis import calculateKurtosis

# file amplitude.py
from amplitude import calculateAmplitude

def viewData(dados):
    ''' Function of plot '''
    sns.jointplot(data=dados)
    plt.show()

    
# this variable is used to read and save the Set type, in csv
conjunto = 'testing'
pasta = conjunto+'/'

# Load data
dados_list, classePotencia, nomeArquivo = load_Data(pasta)

# Calculation of the moving average
media_list = [calculateMoving_average(25, dados_list[i]) for i in range(len(dados_list))]

# calculating the variance
variancia_list = [calculateVariance(25, dados_list[i]) for i in range(len(dados_list))]

# joining two lists using merge
df2_list = [pd.merge(media_list[i], variancia_list[i], right_index = True, left_index = True) for i in range(len(dados_list))]

# Calculating kurtosis
curtose_list = [calculateKurtosis(25,dados_list[i]) for i in range(len(dados_list))]

# join two lists using merge
df3_list = [pd.merge(df2_list[i], curtose_list[i], right_index = True, left_index = True) for i in range(len(dados_list))]

# Call the calculate amplitude function to add to a list
amplitude_list = [calculateAmplitude(dados_list[i],10) for i in range(len(dados_list))]

df1 = pd.DataFrame(amplitude_list)
df2 = pd.DataFrame(classePotencia, columns=['Y'])

# Mapping power class values
df2['Y'] = df2['Y'].map({'A': 0.22, 'B': 0.32, 'C': 0.62, 'D': 1.15, 'E': 0.27, 'F': 0.50, 'G': 0.85, 'H': 1.00})

# Concatenating dataframes
conjuntoDados = pd.concat([df1, df2], axis=1, ignore_index=True)

# Renaming columns
conjuntoDados.columns = list(df1.columns) + ['Y']

# Saving to CSV file
conjuntoDados.to_csv(conjunto+'.csv', index=False)
