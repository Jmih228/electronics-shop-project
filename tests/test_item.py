"""Здесь надо написать тесты с использованием pytest для модуля item."""
import sys
sys.path.append(r'..\src')
import item
import phone
# такой усложненный импорт из-за того, что простое src.item мой пайчарм почему-то не видит

notebooks = item.Item("Ноутбук", 20000, 5)


def test_init():

    assert notebooks.name == "Ноутбук"
    assert notebooks.price == 20000
    assert notebooks.quantity == 5


def test_calculate_price():
    assert notebooks.calculate_total_price() == 100_000


def test_discount_method():
    # устанавливаем новый уровень цен
    item.Item.pay_rate = 0.8
    # применяем скидку
    notebooks.apply_discount()
    assert notebooks.price == 16000.0


def test_instantiate_from_csv():
    item.Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(item.Item.items) == 5  # в файле 5 записей с данными по товарам

    item1 = item.Item.items[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert item.Item.string_to_number('5') == 5
    assert item.Item.string_to_number('5.0') == 5
    assert item.Item.string_to_number('5.5') == 5


def test_name_setter():
    item1 = item.Item("Телефон", 10000, 20)
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'


def test_repr_method():
    item2 = item.Item("Смартфон", 10000, 20)
    assert repr(item2) == "Item('Смартфон', 10000, 20)"


def test_str_method():
    item3 = item.Item("Смартфон", 10000, 20)
    assert str(item3) == 'Смартфон'

def test_phone_class():
    phone1 = phone.Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

def test_add_method():
    item1 = item.Item("Смартфон", 10000, 20)
    phone1 = phone.Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
