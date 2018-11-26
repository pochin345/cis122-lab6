__author__ = ''
__class__ = ''
__crn__ = ''


# a. Describe the program - Animal.py - https://online.pcc.edu/d2l/le/content/233109/viewContent/5274354/View do here.

# b. What is the expect output of Animal.py.

# c. There seem to be bugs preventing Animal.py to produce the correct result as expected.  What are the errors?
#    List them here:

# d. After fixing all the bugs, does Animal.py run correctly and produce the correct result.


class animal:
    _type = "Animal"
    _name = ""
    _weight = 0.0

    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def get_type(self):
        return self._type

    def set_name(self, value):
        self._name = value

    def display(self):
        print("A", self._type, "named", self._name, end="")
        print(" is", self._weight, "pounds")


class dog(Animal):
    _type = "Dog"

    def speak(self):
        print(self._name, "says Woof Woof!")


class cat(Animal):
    _type = "Cat"

    def speak(self):
        print(self._name, "says Meow")


def main():
    snowball = None
    pets = [None] * 3

    snowball = Cat("No name yet", 10.5)
    snowball.set_name("Snowball")

    snowball.display()

    pets = [snowball, Dog("Spot", 30), Cat("Fluffy", 12)]

    print("-- All pets: --")
    for pet in pet:
        pet.display()
        pet.speak()

main()