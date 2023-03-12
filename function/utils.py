from data.class_products import Phone

# смартфон iPhone 14, цена 120_000, количетсво товара 5, симкарт 2
phone1 = Phone('iPhone 14', 120_000, 5, 2)
print(phone1)
# iPhone 14
print(repr(phone1))
# Phone('iPhone 14', 120000, 5, 2)
phone1.number_of_sim = 0
print(repr(phone1))
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
