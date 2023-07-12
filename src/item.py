from csv import DictReader
import sys
sys.path.append(r'../src')

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    items = []

    def __init__(self, __name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param __name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = __name
        self.price = price
        self.quantity = quantity
        self.items.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(self, Item) or isinstance(self, phone.Phone) and isinstance(other, Item) or isinstance(other, phone.Phone):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        Item.items = []
        with open(r'../src/items.csv') as items:
            dict_items = DictReader(items)
            for row in dict_items:
                Item(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(string):
        return int(string.split('.')[0])
