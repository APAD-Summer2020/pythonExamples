class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def __str__(self):
        return f"Rectangle: length = {self.length}, width = {self.width}"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)  # call __init__ in Rectangle class
        #super(Square, self).__init__(length, length) # equivalent

    def __str__(self):
        return f"Square: side = {self.length}"

def main():
    square = Square(4)
    print(square)
    print(f"Area: {square.area()}")

if __name__ == "__main__":
    main()


    
