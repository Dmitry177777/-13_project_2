
class Item ():
    """"Класс категорий товаров"""
    all =[]
    pay_rate = 1

    def __init__(self, categories, price, quantity):
        self.categories = categories  #категория
        self.price = price #цена
        self.quantity = quantity # кол-во
        Item.all.append(Item)


    def calculate_total_price(self):
        """Метод расчета общей стоимости"""

        total_price =self.price*self.quantity

        return total_price


    def apply_discount (self):

        """Метод расчета дискаунта"""

        self.price =self.price*self.pay_rate
        pass
