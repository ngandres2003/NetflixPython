import csv #Importamos la funcion csv

def read_csv(path): #Funcion para leer el archivo de tipo csv. path = archivo.csv
    with open(path,'r') as csvfile: #Abrimos el archivo y lo nombramos como csvfile
        reader = csv.reader(csvfile) #Leemos el archivo
        header = next(reader) #Tomamos los valores de cabecera , iterando nosotros mismos
        data_list = []
        for row in reader: 
            dict_data = dict(zip(header,row)) #Uno la cabera con sus respectivos valores en un dict
            data_list.append(dict_data) #Con los Dict asignados, creo una lista de diccionarios
        return data_list #Retorno la lista de diccionarios
if __name__=='__main__':
    read_csv()
            