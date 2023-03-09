import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
     
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f"./imgs/{name}.png")
    plt.close()

#generando una grafica de pastel

def generate_pie_chart(name, labels, values):
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels) #aqui seleccionamos el tipo de grafica # asi son las reglas del piechart
    ax.axis("equal") #grafica centrada y circular
    plt.savefig(f"./imgs/{name}.png")
    plt.close()



if __name__ == "__main__":

    labels = ["a", "b" ,"c"]
    values = [10, 40, 809]

    #generate_bar_chart(labels, values)

    generate_pie_chart(labels, values)



    
