class Product:
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions


class Customer:
    def __init__(self, surname, name, patronymic, mobile_phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone


class Order:
    def result(self, person, *args):
        list_prices = []
        list_descriptions = []
        list_dimensions = []
        for i in args:
            list_prices.append(i.price)
            list_descriptions.append(i.description)
            list_dimensions.append(i.dimensions)
        return list_prices, ", ".join(list_descriptions), ", ".join(
            [person.surname, person.name, person.patronymic, person.mobile_phone])

    def information(self, product):
        list_products = [str(product.price), product.description, str(product.dimensions)]
        return ", ".join(list_products)


orange = Product(3, "orange", 1)
apple = Product(2, "apple", 1)
salt = Product(13, "salt", 1)

Max = Customer("Bredyuk", "Maksim", "Oleksandrovich", "+380972756288")
David = Customer("Bondar", "David", "Vitaliyovich", "+380956385033")

order = Order()
print(f"Information about the person: {order.result(David, orange, apple, salt)[2]}\n"
      f"Shopping list: {order.result(David, orange, apple, salt)[1]}\n"
      f"Purchase price: {sum(order.result(David, orange, apple, salt)[0])}")
print(f"\n\n\nPrice list:\n"
      f"{order.information(orange)}\n"
      f"{order.information(apple)}\n"
      f"{order.information(salt)}")

