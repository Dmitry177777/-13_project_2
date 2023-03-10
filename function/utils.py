from data.class_products import Item
# import os.path
# import sys
# file_dir = os.path.dirname('E:\Python_SqyPro\\4_object_oriented_programming\project_1\data\class_products.py')
# sys.path.append(file_dir)



item = Item('Телефон', 10000, 5)
item.name = 'Смартфон'
print(item.name)
# Смартфон

item.name = 'СуперСмартфон'
# Exception: Длина наименования товара превышает 10 символов.

f = 'project_1\data\items.csv'
Item.instantiate_from_csv(f)  # создание объектов из данных файла
print(len(Item.all))  # в файле 5 записей с данными по товарам
# 5
item1 = Item.all[0]
print(item1.name)
# Смартфон


# print(Item.is_integer(5))
# print(Item.is_integer(5.0))
# print(Item.is_integer(5.5))
# True
# True
# False
