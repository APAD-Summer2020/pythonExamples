class Person:
    """ Instantiates a Person object with given name.
    This is a docstring - a multi-line comment.
    """

    def __init__(self, first_name, last_name): # like Java constructor
        self.first = first_name
        self.last = last_name

    def __str__(self):
        return self.first + " " + self.last

    def getFirst(self):
        return self.first

    def getLast(self):
        return self.last

def main():
    p1 = Person("Pinkie", "Pie")
    print(p1)
    p1.first = "Pink"
    print(p1)

if __name__ == '__main__':
    main()

