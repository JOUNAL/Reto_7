class RegisterOrdersIterator:
  def __init__(self, list_order):
    self.list_iter = list_order
    self.indice = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.indice < len(self.list_iter):
      item_order = self.list_iter[self.indice]
      self.indice += 1
      return item_order
    else:
      raise StopIteration



class Order:
    def __init__(self):
        self.list =[]

    def total_price(self):
        self.total = sum([item.subtotal for item in self.list])
        return self.total

    def discount(self, discount):
        self.total = sum([item.subtotal for item in self.list])
        self.total -= self.total * (discount / 100)
        return self.total

    def add_item(self, item):
        self.list.append(item)

    def get_list(self):
        ([item.name for item in self.list])
        print("Nombre                 Precio")
        for item in self.list:
            print(f"{item.name} x {item.quantity}    {item.price}")
        
    def __iter__(self):
        return RegisterOrdersIterator(self.list)


class MenuItem:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.subtotal= self.price*self.quantity

class Juice(MenuItem):
    def __init__(self, name, price,quantity,sugar):
        super().__init__(name, price,quantity)
        self.sugar=sugar

class Soup(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.kind=kind
        
class Soda(MenuItem):
    def __init__(self, name, price,quantity,sugar):
        super().__init__(name, price,quantity)
        self.sugar=sugar
        
class IceCream(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.sugar=kind
        
class Beer(MenuItem):
    def __init__(self, name, price,quantity,brand):
        super().__init__(name, price,quantity)
        self.brand=brand
        
class Sandiwch(MenuItem):
    def __init__(self, name, price,quantity,protein):
        super().__init__(name, price,quantity)
        self.protein=protein
        
class MainDish(MenuItem):
    def __init__(self, name, price,quantity,description):
        super().__init__(name, price,quantity)
        self.description=description
        
class Beef(MenuItem):
    def __init__(self, name, price,quantity,grams):
        super().__init__(name, price,quantity)
        self.grams=grams
        
class SideDish(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.kind=kind
        
class Appetizer(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.kind=kind

orden_1=Order()

orden_1.add_item(Juice(name="Jugo de mango",price=2000,quantity=3,sugar="No"))
orden_1.add_item(Soup(name="Sancocho de pescado",price=4000,quantity=2,kind="Sancocho"))
orden_1.add_item(MainDish(name="Cerdo a la llanera",price=9000,quantity=2,description="Cerdo con salsa de la casa, arroz, patacon y ensalada"))
orden_1.add_item(Appetizer(name="Parfait",price=3500,quantity=2,kind="Dulce"))

print("El precio total de la orden es:" + str(orden_1.total_price()))
orden_1.get_list()


for item_order in orden_1:
  objecto=list(item_order)
  print(f"Nombre:{item_order.name} Precio_u:{item_order.price} Cantidad:{item_order.quantity}")