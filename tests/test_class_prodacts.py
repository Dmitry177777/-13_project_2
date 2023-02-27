from data.class_products import Item

def test_init():
   assert Item.__init__("Смартфон", 10000, 20) == ""
   assert Item.__init__("Ноутбук", 20000, 5) == ""


def test_calculate_total_price(self):
    assert Item.calculate_total_price(self) == self.price*self.quantity


def apply_discount(self):
    assert Item.apply_discount(self) == self.price*self.pay_rate
