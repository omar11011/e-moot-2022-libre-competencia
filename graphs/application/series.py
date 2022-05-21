import pandas as pd
import matplotlib.pyplot as plt

def ApplicationSeries():
    sheets = ["users", "affiliates", "collaborators"]

    for sheet in sheets:   
        # Exportamos la base de datos
        df = pd.read_excel('data/application.xlsx', sheet_name=sheet)

        # Apps de Delivery
        apps = df.groupby('App').nunique().reset_index()['App'].values

        # Comenzamos a graficar
        fig, ax = plt.subplots()

        # Contador y colores
        count = 0
        colors = ['r', 'g', 'b', 'k']

        # Graficamos para cada Aplicación
        for app in apps:
            x = (df[df["App"] == app]["Year"]).values
            y = (df[df["App"] == app]["Total"]).values
            ax.plot(x,  y, color = colors[count], label=app)
            plt.gcf().set_size_inches(9, 7)
            count += 1
        
        plt.xlabel("Year")
        plt.ylabel('Number ' + sheet.capitalize() +' (in thousands)')
        plt.title('Number of Application ' + sheet.capitalize())
        plt.legend(shadow=True, title="Supermarket")
        plt.savefig('./img/plot-' + sheet + '.png')