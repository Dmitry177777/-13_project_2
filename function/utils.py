from data.class_products import Item

# from data.class_products import Phone

# адрес файла
f = '..\data\items.csv'
# Файл items.csv отсутствует.
Item.instantiate_from_csv(f)
# файл ..\data\items.csv загружен

# адрес файла
f = '..\data\items2.csv'
# Файл items.csv отсутствует.
Item.instantiate_from_csv(f)
# FileNotFoundError: Отсутствует файл item2.csv

f = '..\data\items1.csv'
# В файле items.csv удалена последняя колонка.
Item.instantiate_from_csv(f)
# InstantiateCSVError: Файл item1.csv поврежден

# kb = KeyBoard('Dark Project KD87A', 9600, 5)
# print(kb)
# # Dark Project KD87A
# print(kb.language)
# # EN
#
# kb.change_lang()
# print(kb.language)
# # RU
# #
# kb.language = 'CH'

# AttributeError: property 'language' of 'KeyBoard' object has no setter


# # смартфон iPhone 14, цена 120_000, количетсво товара 5, симкарт 2
# phone2 = Item('iPhone 14', 120_000, 5)
# print(repr(phone2))
#
# phone1 = Phone('iPhone 14', 120_000, 5, 2)
# print(phone1)
# # iPhone 14
# print(repr(phone1))
# # Phone('iPhone 14', 120000, 5, 2)
# # print (phone1.number_of_sim)
# phone1.number_of_sim = 0
# print(repr(phone1))
# ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.


# item = Item('Телефон', 10000, 5)
# item.name = 'Смартфон'
# print(item.name)
# # Смартфон
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
