import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["A", "B", "C"]
    values = [200,34,123]

    fig, ax = plt.subplots()
    ax.pie(values, labels =labels)
    plt.savefig("pie.png") #para generar la grafica y guardar la grafica como pie.png
    plt.close()