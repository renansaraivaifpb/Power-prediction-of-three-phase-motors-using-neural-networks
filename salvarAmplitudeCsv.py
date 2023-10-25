def salvarAmplitudeCSV(amplitude_list_):
    import csv
# Open the file in writing mode
    with open('arquivo.csv', mode='w', newline='') as arquivo:
        # Create a CSV write object
        escritor = csv.writer(arquivo)
        # Write headers to CSV file
        escritor.writerow(['amplitude_X', 'amplitude_Y', 'amplitudeZ'])

        # For each row of the data list
        for linha in amplitude_list_:
            # Add the header to the line and write the line to the CSV file
            escritor.writerow(linha)
