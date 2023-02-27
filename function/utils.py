from data.class_products import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
#200000  # общая стоимость смартфонов
#100000  # общая стоимость ноутбуков

Item.pay_rate = 0.8  # устанавливаем новый уровень цен
item1.apply_discount()
print(item1.price)
print(item2.price)
#8000.0  # к цене смартфона применена скидка
#20000  # к цене ноутбука скидка не была применена

print(Item.all)
#[<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]