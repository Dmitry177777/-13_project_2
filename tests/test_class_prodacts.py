from data.class_products import Item
from data.class_products import Phone

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
item3 = Item("Ручка", 2200, 5.5)
all = []
pay_rate = 1

f = '..\data\items.csv'
item_all = [{'_name': 'Смартфон', 'price': 10000, 'quantity': 20},
            {'_name': 'iPhone 14', 'price': 120000, 'quantity': 5},
            {'_name': 'Смартфон', 'price': '100', 'quantity': '1'},
            {'_name': 'Ноутбук', 'price': '1000', 'quantity': '3'},
            {'_name': 'Кабель', 'price': '10', 'quantity': '5'},
            {'_name': 'Мышка', 'price': '50', 'quantity': '5'},
            {'_name': 'Клавиатура', 'price': '75', 'quantity': '5'}
            ]

phone1 = Phone('iPhone 14', 120_000, 5, 2)


def test_init():
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20

    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2

    # Item.all.append(Item)


def test_calculate_total_price():
  assert item1.calculate_total_price() == item1.price * item1.quantity
  assert item2.calculate_total_price() == item2.price * item2.quantity


def test_apply_discount():
  discount_price = item1.price * item1.pay_rate
  item1.apply_discount()
  assert item1.price == discount_price


def test_is_integer():
    assert item1.is_integer(item1.quantity) == True
    assert item2.is_integer(item2.quantity) == True
    assert item3.is_integer(item3.quantity) == False


def test_instantiate_from_csv():
    assert Item.instantiate_from_csv(f) == item_all


def test__repr__():
    assert item1.__repr__() == f'Item(Смартфон, 10000, 20)'
    assert item2.__repr__() == f'Item(Ноутбук, 20000, 5)'
    assert item3.__repr__() == f'Item(Ручка, 2200, 5.5)'


def test__str__():
    assert item1.__str__() == f'Смартфон'
    assert item2.__str__() == f'Ноутбук'
    assert item3.__str__() == f'Ручка'
