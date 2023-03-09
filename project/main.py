import own_modules
import readcsv
import charts

def run():
    
    data = readcsv.read_csv("./data.csv") #devuelve la data de paises en un dict

    #seleccionamos pais
    country = input("type country of choice: ")
    
    result = own_modules.population_by_country(data, country)


    if len(result) >0: # si encuentra el pais :
        country= result[0]
        
        labels, values = own_modules.get_population(country)
        
        #para graficar la poblacion por pais

        charts.generate_bar_chart(country["Country/Territory"], labels, values)

        #generar grafica con codigos de pais y porcentajes de poblacion
        """ codes, world_population= own_modules.country_codes_and_world_pop(data)
        charts.generate_pie_chart(country["Country/Territory"], codes, world_population) """
    
    #solucion de platzi para hacer el piechart con los porcentajes
    """ countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages) """

if __name__ == "__main__":
    run()

""" Este if le dice al main.py, que si el archivo es ejecutado desde la terminal, 
ejecute el metodo run, pero si es ejecutado desde otro archivo, el metodo run 
no se ejecutaria. """