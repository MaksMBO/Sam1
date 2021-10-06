class Rectangle(object):
    def __init__(self):
        self.length = 1
        self.width = 1

    def set(self, lgth, wid):
        self.length = lgth
        self.width = wid
        if not self.length <= 20 or not self.length > 0:
            self.length = 1
        if not self.width <= 20 or not self.width > 0:
            self.width = 1

    def get(self):
        return self.length, self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def square(self):
        return self.length * self.width


try:
    rectangle = Rectangle()
    length = float(input("Length: "))
    width = float(input("Width: "))

    rectangle.set(length, width)
    print(f"Length: {rectangle.get()[0]} \nWidth: {rectangle.get()[1]}")
    print(f"Perimeter: {rectangle.perimeter()}")
    print(f"Square: {rectangle.square()}")
except ValueError:
    print("You did not enter incorrect data!")
