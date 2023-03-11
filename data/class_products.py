import csv
class Item ():
    """"Класс категорий товаров"""
    all = []
    pay_rate = 1

    def __init__(self, name: str, price, quantity):
        self.name = name  # наименование
        self.price = price  # цена
        self.quantity = quantity  # кол-во

    @property
    def name(self):
        dict_i = {
            'name': self._name,
            'price': self.price,
            'quantity': self.quantity
        }
        dict_ii = dotdict(dict_i)
        Item.all.append(dict_ii)
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
            i = [cls(row['name'], row['price'], row['quantity']).name for row in reader]

        return

    def calculate_total_price(self):
        """Метод расчета общей стоимости"""

        total_price = self.price * self.quantity

        return total_price


    def apply_discount (self):

        """Метод расчета дискаунта"""

        self.price = self.price * self.pay_rate

        return


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
