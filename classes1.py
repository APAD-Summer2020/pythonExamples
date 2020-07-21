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

class SuperHero(Person):
    def __init__(self, first, last, nick):
        super(SuperHero, self).__init__(first, last)
        self.nick = nick

    def nick_name(self):
        return f"I am {self.nick}"

def main():
    p1 = Person("Pinkie", "Pie")
    print(p1)
    p1.first = "Pink"
    print(p1)

    #  another person
    p2 = SuperHero("Clark", "Kent", "Superman")
    print(p2.nick_name())
    print(p2.first)

    # what is that __name__ thing??
    print(__name__)                # __main__ is default namespace in Python

    # type, isinstance stuff
    print(f"The type of p2 is {type(p2)}")  # <class '__main__.SuperHero'>
    print(type(p2) is SuperHero)            # True
    print(isinstance(p2, SuperHero))        # True
    print(isinstance(p2, Person))           # True
    
    

if __name__ == '__main__':                 # True if we're running this file
    main()
