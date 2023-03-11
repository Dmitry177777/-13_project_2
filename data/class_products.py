import csv
class Item ():
    """"Класс категорий товаров"""
    all = []
    pay_rate = 1

    def __init__(self, name: str, price, quantity):
        self.name = name # наименование
        self.price = price  # цена
        self.quantity = quantity  # кол-во


    @property
    def name(self):
        Item.all.append(self._name)
        return self._name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) <= 10 and isinstance(new_name, str):
            self._name = new_name
        else:
            print("Название товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls, f):
        """выгрузка и инициализация данных из файла csv"""

        # fieldnames = ['name', 'price', 'quantity']
        with open(f, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            [cls(row['name'],row['price'],row['quantity']).name for row in reader]

        return

    def calculate_total_price(self):
        """Метод расчета общей стоимости"""

        total_price = self.price * self.quantity

        return total_price


    def apply_discount (self):

        """Метод расчета дискаунта"""

        self.price = self.price * self.pay_rate

        return
