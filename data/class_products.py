import csv
class Item ():
    """"Класс категорий товаров"""
    all = []
    pay_rate = 1

    def __init__(self, name, price, quantity):
        self._name = name  # наименование
        self.price = price  # цена
        self.quantity = quantity  # кол-во
        Item.all.append(Item)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10 and isinstance(new_name, str):
            self._name = new_name
        else:
            print("Название товара превышает 10 символов")

    @staticmethod
    def instantiate_from_csv(f):
        """выгрузка и инициализация данных из файла csv"""

        fieldnames = ['name', 'price', 'quantity']
        with open(f, 'w', newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames, restkey=None, dialect='excel')
            print(reader)
        pass

    def calculate_total_price(self):
        """Метод расчета общей стоимости"""

        total_price = self.price * self.quantity

        return total_price


    def apply_discount (self):

        """Метод расчета дискаунта"""

        self.price = self.price * self.pay_rate

        return
