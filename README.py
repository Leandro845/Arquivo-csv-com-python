# Arquivo-csv-com-python
Criando um arquivo csv utilizando python

import csv


with open('file.csv', 'w') as f: #Create the file csv
    write = csv.writer(
        f, #Arquivo
        delimiter=',', #Delimiter
        quotechar='"', #Quote character
        quoting=csv.QUOTE_ALL #To select quotes in all values
    )

    #Add name to values
    write.writerow(
        [
            'NAME',
            'LAST NAME',
            'FONE',
            'EMAIL'
        ]
    )

    #Add the values
    write.writerow(
        [
            'MY NAME',
            'MY LAST NAME',
            'MY FOONE',
            'MY EMAIL'
        ]
    )
