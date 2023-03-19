import csv


class Item():
    """"Класс категорий товаров"""
    all = []
    pay_rate = 1

    def __init__(self, name: str, price, quantity):
        self._name = name  # наименование
        self.price = price  # цена
        self.quantity = quantity  # кол-во

    def __repr__(self):
        return f'Item({self.name}, {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.name}'

    @property
    def name(self):
        dict_i = {
            '_name': self._name,
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

                cls.all.append(cls(row_name, row_price, row_quantity).__dict__)
        return cls.all
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


class Phone(Item):
    """ новый наследуемый класс"""

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim_ = number_of_sim  # сим
        # if isinstance(number_of_sim, int) and (number_of_sim > 0):
        #     self.number_of_sim = number_of_sim  # сим
        # else:
        #     return ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

    @property
    def number_of_sim(self):
        return self.number_of_sim_

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        if isinstance(new_number_of_sim, int) and new_number_of_sim > 0:
            self.number_of_sim_ = new_number_of_sim  # сим
            return
        else:
            return ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

    def __repr__(self):
        return f'Phone({self.name}, {self.price}, {self.quantity},{self.number_of_sim})'

    def __str__(self):
        return f'{self.name}'


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
