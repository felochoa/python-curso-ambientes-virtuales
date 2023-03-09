# los moldulos son cualquier archivo que termine en .py
#cualquiera se puede comportar como modulo


A= "hola"

def population_by_country (data, country):
    
    # filtramos por data que es un dict buscamos el pais, country viene de un input
    result = list(filter(lambda item : item["Country/Territory"] == country, data))
    return result

#aqui se hace la solucion del reto segun el profesor
# mi solucion está en country_of_study.py

def country_codes_and_world_pop(data):
    c_codes = [] 
    world_pop =[] 
    for dictionaries in data:        
        #labels serán los codigos de los paises
        c_codes.append(dictionaries["CCA3"])
        # los valores de la grafica serán los porcentajes de poblacion mundial
        world_pop.append(dictionaries["World Population Percentage"])
  
    codes = c_codes
    world_population = world_pop
    return codes , world_population

def get_population(country_dict):
    population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

## ideas de expansion del proyecto
## que el usuario pueda escoger lo que quiere graficar - columma vs codigo de pais o pais
## que pueda sacar la grafica de cada label de columna que sea numerico
## 