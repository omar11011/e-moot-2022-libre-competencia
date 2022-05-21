# Importamos los módulos creados para graficar
from graphs.tickets.averagePrice import AverageTicketPrice
from graphs.tickets.averageTotal import AverageTotalTickets
from graphs.application.series import ApplicationSeries
from graphs.application.bar import ApplicationBar
from graphs.satisfaction.bar import SatisfactionGraph

if __name__ == "__main__":
    AverageTicketPrice()
    AverageTotalTickets()
    ApplicationSeries()
    ApplicationBar()
    SatisfactionGraph()