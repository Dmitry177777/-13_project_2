import csv


class Item():
    """"Класс категорий товаров"""
    all = []
    pay_rate = 1

    def __init__(self, name: str, price, quantity):
        self.name = name  # наименование
        self.price = price  # цена
        self.quantity = quantity  # кол-во

    def __repr__(self):
        return f'Item({self.name}, {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.name}'

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

            for row in reader:
                row_name = row['name']
                row_price = row['price']
                row_quantity = row['quantity']
                if Item.is_integer(row_price):
                    row_price = int(row_price)
                if Item.is_integer(row_quantity):
                    row_quantity = int(row_quantity)

                i = cls(row_name, row_price, row_quantity).name
        return

    def calculate_total_price(self):
        """Метод расчета общей стоимости"""

        total_price = self.price * self.quantity

        return total_price

    def apply_discount(self):

        """Метод расчета дискаунта"""

        self.price = self.price * self.pay_rate

        return

    @staticmethod
    def is_integer(x):
        # isInt = isinstance(number, int)
        isInt = int(x) == x
        return isInt  # True

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError('Запрещена операция с экземплярами классов не родственных Item')


class Phone(Item):
    def __int__(self, name, price, quantity, number_of_sim: int, a):
        super().__init__(name, price, quantity)
        self.a = a
        if isinstance(number_of_sim, int) and number_of_sim > 0:
            self.number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
