class Product:
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions

    @property
    def price(self):
        return self.__price

    @property
    def description(self):
        return self.__description

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("The value must be a number")
        self.__dimensions = value

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("The value must be a string")
        self.__description = value

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError("The value must be a number and greater than zero")
        self.__price = value

    def __str__(self):
        return f"{self.description} = {self.__price}"


class Customer:
    def __init__(self, surname, name, patronymic, mobile_phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError("The value must be a string")
        self.__surname = value

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def mobile_phone(self):
        return self.__mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        if not isinstance(value, str):
            raise ValueError('The value must be a string')
        self.__mobile_phone = value

    @patronymic.setter
    def patronymic(self, value):
        if not isinstance(value, str):
            raise TypeError("The value must be a string")
        self.__patronymic = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("The value must be a string")
        self.__name = value


class Order:
    def __init__(self, person, *products):
        self.person = person
        self.products = products

    @property
    def person(self):
        return self.__person

    @person.setter
    def person(self, value):
        if not value:
            raise TypeError("No value")
        self.__person = value

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, value):
        if not value:
            raise TypeError("No value")
        self.__products = value

    def result(self):
        list_prices = []
        list_descriptions = []
        list_dimensions = []
        for i in self.__products:
            list_prices.append(i.price)
            list_descriptions.append(i.description)
            list_dimensions.append(i.dimensions)
        return list_prices, ", ".join(list_descriptions), ", ".join(
            [self.__person.surname, self.__person.name, self.__person.patronymic, self.__person.mobile_phone])

    def add(self):
        return sum(self.result()[0])

    def about_person(self):
        return self.result()[2]

    def about_list(self):
        return self.result()[1]


orange = Product(3, "orange", 1)
apple = Product(2, "apple", 1)
salt = Product(13, "salt", 1)
David = Customer("Bondar", "David", "Vitaliyovich", "+380956385033")
order = Order(David, orange, apple, salt, apple)

print(f"Information about the person: {order.about_person()}\n"
      f"Shopping list: {order.about_list()}\n"
      f"Purchase price: {order.add()}\n"
      f"\nProduct information:\n"
      f"{orange}\n"
      f"{apple}\n"
      f"{salt}"
      )

