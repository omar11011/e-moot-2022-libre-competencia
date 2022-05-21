import pandas as pd
import matplotlib.pyplot as plt

def AverageTicketPrice():
    # Exportamos la base de datos
    df = pd.read_excel('data/tickets.xlsx', sheet_name='Sheet1')
    # Lista con los nombres de las tiendas
    market = ["Goreiro", "Tiendas Genovia", "La Canasta", "Otros"]
    # Colores a usar para el gráfico
    color = ["r","b","g","k"]
    # Contador para variar en la elección de los colores
    countColor = 0

    fig, ax = plt.subplots()
    
    # Ciclo que graficará por cada tienda
    for i in market:
        x = (df[df["Market"] == i]["Date"]).values
        y = (df[df["Market"] == i]["Price"]).values
        ax.plot(x,  y, color = color[countColor], label=i)
        plt.gcf().set_size_inches(9, 7)
        countColor += 1
    
    # Completando el gráfico
    plt.xlabel("Date")
    plt.ylabel("Average Price")
    plt.title("Average Ticket Price in Supermarkets")
    plt.legend(shadow=True, title="Market")
    plt.savefig("./img/average-price.png")