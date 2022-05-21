import pandas as pd
import matplotlib.pyplot as plt

def ApplicationBar():
    sheets = ["users", "affiliates", "collaborators"]

    for sheet in sheets:
        # Exportamos la base de datos
        df = pd.read_excel('data/application.xlsx', sheet_name=sheet)

        # Apps de Delivery
        data = df.groupby(['App'])['Total'].mean()
        apps = df.groupby('App').nunique().reset_index()['App'].values

        # Comenzamos a graficar
        fig, ax = plt.subplots()
        ax.bar(apps, list(data.values))

        plt.xlabel('Applications')
        plt.ylabel('Number of Application ' + sheet.capitalize() + ' (in thousands)')
        plt.title('Average Number of Application ' + sheet.capitalize() + ' (2015 - 2022)')
        plt.savefig('./img/bar-' + sheet + '.png')