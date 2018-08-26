import math
def pizza_optima(listaDePizzas):

    pizzaOptima = listaDePizzas[0]
    for pizza in listaDePizzas:
        if pizza.ratio < pizzaOptima.ratio:
            pizzaOptima = pizza

    return pizzaOptima

class Pizza:
    radio = 0.00
    precio = 0.00
    area = 0.00
    ratio = 0.00

    def __init__(self, radio, precio):
        self.radio = radio
        self.precio = precio
        self.area = math.pi*pow(radio,2)
        self.ratio = precio/self.area



    

    