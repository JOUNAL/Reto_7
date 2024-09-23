# Reto_7
Iteradores

# Programación Orientada a Objetos - UNAL

## Reto 7

Para este reto se utilizaron el codigo realizado en el reto 3.2, donde solo se implementara una nueva clase, la cual hara de iterable en todo los items de una orden

### Codigo clase iterable

La clase implementada fue la siguiente
Codigo:

```python
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
```

### Codigo clase Order
Y para que pudiera funcionar se le implemento un nuevo metodo a la clase Order, para que puede ser un objeto Order tenga la capacidad de poder iterarse, quedando la clase de la siguiente manera

Codigo:

```python
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
```

### Visualizando

Y ahora un ejemplo para poder visualizar mejor todo esto, tenemos los siguientes items que formaran la orden
Codigo:

```python
orden_1.add_item(Juice(name="Jugo de mango",price=2000,quantity=3,sugar="No"))
orden_1.add_item(Soup(name="Sancocho de pescado",price=4000,quantity=2,kind="Sancocho"))
orden_1.add_item(MainDish(name="Cerdo a la llanera",price=9000,quantity=2,description="Cerdo con salsa de la casa, arroz, patacon y ensalada"))
orden_1.add_item(Appetizer(name="Parfait",price=3500,quantity=2,kind="Dulce"))
```

Y la salida que nos das el codigo (Un poco modificada para mayor entendimiento de que se esta iterando en ese momento) seria
Output:

```
Nombre:Jugo de mango Precio_u:2000 Cantidad:3
Nombre:Sancocho de pescado Precio_u:4000 Cantidad:2
Nombre:Cerdo a la llanera Precio_u:9000 Cantidad:2
Nombre:Parfait Precio_u:3500 Cantidad:2
```

(Para mayor detalle, revisar el archivo Menu_class.py)
Muchas Gracias por leer.

