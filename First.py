class Rectangle(object):
    def __init__(self):
        self.__length = 1
        self.__width = 1

    @property
    def get(self):
        return self.__length, self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def area(self):
        return self.__length * self.__width

    @get.setter
    def set(self, val):
        self.__length = val[0]
        self.__width = val[1]
        if not self.__length <= 20 or not self.__length > 0:
            self.__length = 1
        if not self.__width <= 20 or not self.__width > 0:
            self.__width = 1


rectangle = Rectangle()

length = input("Length: ")
if not length.isdecimal():
    raise ValueError("You did not enter incorrect data!")
length = float(length)

width = input("Width: ")
if not width.isdecimal():
    raise ValueError("You did not enter incorrect data!")
width = float(width)

values = [length, width]
rectangle.set = values
print(f"Length: {rectangle.get[0]} \nWidth: {rectangle.get[1]}")
print(f"Perimeter: {rectangle.perimeter()}")
print(f"Square: {rectangle.area()}")
