import csv
import string
# quiero que segun la sigla del pais me saque los datos de la población 

# el usuario da la sigla del pais segun el codigo CCA del pais

#idea para sacar los datos de la población



def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter= ",") # los datos estan separados por , por ser csv
        
        data = []
        
        country_codes=[]
        
        country_data ={}
        

        header = next(reader)
        
        
        
        #generamos lista con todos los coidgos CCA3 de los paises y lista con los diccionarios de todos los paises
        for filas in reader:
            iterable_1 = zip(header,filas)
            
            
            country_codes_data = { key : value for key, value in iterable_1 }
            
            #generamos lista con codigos de los paises
            country_codes.append(country_codes_data["CCA3"])
            
            #llenamos la lista con los diccionarios
            data.append(country_codes_data)

                   

        #hacer que el usuario elija el codigo del pais:
        print("Escoge el país para mostrar los datos de la población \n") 
        
        prompt= input("ingresa el código CCA3 del país: ")
        country_of_choice= prompt.upper() #convertir a mayusculas
        
        #print(country_of_choice)
        
        if not country_of_choice in country_codes:
            while(True):
                prompt=input("el texto ingresado no coincide con un código CCA3, intenta de nuevo: ")
                country_of_choice= prompt.upper()
                if country_of_choice in country_codes:
                    break

        
        #debemos recorrer cada diccionario en data y buscar el pais del
        for diccionarios in data:

            for key in diccionarios:
                
                #encontrando el codigo del pais
                if diccionarios["CCA3"] == country_of_choice:
                                       
                    #preguntamos cuales llaves del diccionario empiezan por un numero (para esto la libreria string)
                    if key[0].isdigit():
                        
                        #solo debemos dejar el numero del año
                        split_key= key.split()

                        #le adicionamos al diccionario los datos asi año : poblacion
                        country_data[split_key[0]]= int(diccionarios[key]) 

        return country_data


#quiero ejecutrar el archivo como un script

if __name__ == "__main__":
    result = read_csv("./data.csv")    
    
    print(result)