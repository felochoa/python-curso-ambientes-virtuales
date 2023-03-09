
import csv

def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter= ",") # los datos estan separados por , por ser csv
        
        #como reader es un iterable podemos obtener la primera fila asi
        header = next(reader)
        #print(header)
        data = []
        
        for row in reader:
            iterable = zip(header,row) #unimos los campos de la primera fila con el corresponmdiente de cada fila
                           
            
            #generamos un dictionario con el iterable
            country_dict = { key : value for key, value in iterable }
    
            #agregando cada diccionario a una lista
            data.append(country_dict)
        return data


#quiero ejecutrar el archivo como un script

if __name__ == "__main__":
    data = read_csv("data.csv")    
    
    #la idea es transformar esto a un diccionario para que sea mas facil de leer
    # la llave del diccionario sera la llave de la columna

    