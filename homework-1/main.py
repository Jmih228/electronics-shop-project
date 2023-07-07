import sys
sys.path.append(r'../src')
from item import Item
# такой усложненный импорт из-за того, что простое src.item мой пайчарм почему-то не видит

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    print(item1.calculate_total_price())  # 200000
    print(item2.calculate_total_price())  # 100000

    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    print(item1.price)  # 8000.0
    print(item2.price)  # 20000

    # изменил название атрибута с экземплярами т.к. пайчарм ругался на него, как на функцию "all"
    print(Item.items)  # [<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]
