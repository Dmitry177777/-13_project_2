from data.class_products import Item

item = Item('Телефон', 10000, 5)
item.name = 'Смартфон'
print(item.name)
# Смартфон
#
#
# print(repr(item))
# # Смартфон
# print(item)
# # Смартфон
#
# item.name = 'СуперСмартфон'
# # Exception: Длина наименования товара превышает 10 символов.
#
# f = '..\data\items.csv'
# # E:\Python_SqyPro\\4_object_oriented_programming\project_1\
# Item.instantiate_from_csv(f)  # создание объектов из данных файла
# print(len(Item.all))  # в файле 5 записей с данными по товарам
# # 5
# print(Item.all)
# item1 = Item.all[0]
#
# print(item1.name)
# # Смартфон
#
#
# print(Item.is_integer(5))
# print(Item.is_integer(5.0))
# print(Item.is_integer(5.5))
# # True
# # True
# # False
