import pandas as pd
import matplotlib.pyplot as plt

def AverageTotalTickets():
    # Exportamos la base de datos
    df = pd.read_excel('data/tickets.xlsx', sheet_name='Sheet2')
    # Lista con los nombres de las tiendas y años
    market = ["Goreiro", "Tiendas Genovia", "La Canasta", "Otros"]
    # Contador para variar en la elección de los colores
    count = 0

    content = []

    fig, ax = plt.subplots(2, 2, sharey = True)
    
    # Ciclo que graficará por cada tienda
    for i in market:
        x = (df[df["Market"] == i]["Date"]).values
        y = (df[df["Market"] == i]["Tickets"]).values
        content.append([x, y])
        count += 1
    
    ax[0,0].plot(content[0][0], content[0][1], "r")
    ax[0,1].plot(content[1][0], content[1][1], "g")
    ax[1,0].plot(content[2][0], content[2][1], "b")
    ax[1,1].plot(content[3][0], content[3][1], "k")
    
    plt.savefig("./img/average-total.png")