import sys
sys.path.append(r'../src')
from item import Item

# такой усложненный импорт из-за того, что простое src.item мой пайчарм почему-то не видит

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.items) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.items[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
