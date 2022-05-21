import pandas as pd
import matplotlib.pyplot as plt

def SatisfactionGraph():
    sheets = ["user", "affiliate", "dealer"]

    for sheet in sheets:
        # Exportamos la base de datos
        df = pd.read_excel('data/satisfaction.xlsx', sheet_name=sheet)

        fig, ax = plt.subplots()
        ax.bar(df['Aplicativo'], df['Porcentaje'])

        plt.xlabel('Application')
        plt.ylabel('Percentage of users who gave 5 stars')
        plt.title(sheet.capitalize() + ' Satisfaction Percentage')
        plt.savefig('./img/' + sheet + '-satisfaction.png')