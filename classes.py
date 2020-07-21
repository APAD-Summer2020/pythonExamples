class Dog:
    genus = "Canis"                         # class variable (immutable)
    activities = ["eat", "sleep", "bark"]   # class variable (mutable)

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        return f'I am {self.name}, a {self.breed}, {self.age} years old'

    def speak(self):
        print("woof")

charlie = Dog("Charlie", "lab", 13)
milo = Dog("Milo", "heeler", 0.5)

print(charlie)
print(milo)

print(milo.activities)
milo.activities.append("play")     # changed activities of all Dogs

print(charlie.activities)

milo.genus = "something else"     # added a new instance variable for milo
print(charlie.genus)       
print(milo.genus)                 
print(Dog.genus)
    
