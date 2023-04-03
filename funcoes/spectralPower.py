import numpy as np

# Skewness (assimetria) de uma distribuição de dados
def calcularSpectralPower(dados_,fs):
    
    # assuming 'accX', 'accY', 'accZ' are lists or numpy arrays containing the raw data
    # assuming the sampling rate is 'fs' in Hz
    # assuming the length of the signals is 'n'

    # calculate the length of the signals
    n = len(dados_)

    # apply FFT to each signal
    X = np.fft.fft(dados_['accX'])
    Y = np.fft.fft(dados_['accY'])
    Z = np.fft.fft(dados_['accZ'])

    # compute the magnitude spectrum of each signal
    mag_X = np.abs(X[:n//2])
    mag_Y = np.abs(Y[:n//2])
    mag_Z = np.abs(Z[:n//2])

    # compute the power spectrum of each signal
    dados_['accX Spectral Power'] = (mag_X**2) / (n*fs)
    dados_['accY Spectral Power'] = (mag_Y**2) / (n*fs)
    dados_['accZ Spectral Power'] = (mag_Z**2) / (n*fs)
    return n