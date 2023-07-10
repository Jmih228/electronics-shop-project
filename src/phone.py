import sys
sys.path.append(r'../src')
import item

class Phone:

    def __init__(self, __name, price, quantity, __number_of_sim):
        self.__name = __name
        self.price = price
        self.quantity = quantity
        self.__number_of_sim = __number_of_sim

    def __repr__(self):
        return f"Phone('{self.__name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(self, item.Item) or isinstance(self, Phone) and isinstance(other, item.Item) or isinstance(other, Phone):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            print('ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.')
