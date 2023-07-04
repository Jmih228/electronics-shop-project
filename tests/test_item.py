"""Здесь надо написать тесты с использованием pytest для модуля item."""
import sys
sys.path.append(r'C:\Users\Hp\PycharmProjects\section4hw_esp\electronics-shop-project\src')
from item import Item
# такой усложненный импорт из-за того, что простое src.item мой пайчарм почему-то не видит

notebooks = Item("Ноутбук", 20000, 5)


def test_init():

    assert notebooks.name == "Ноутбук"
    assert notebooks.price == 20000
    assert notebooks.quantity == 5


def test_calculate_price():
    assert notebooks.calculate_total_price() == 100_000


def test_discount_method():
    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    notebooks.apply_discount()
    assert notebooks.price == 16000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.items) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.items[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
