from animal import Animal
# inheritance
class Dog(Animal):

    def __init__(self, dog_name, dog_colour):
        # calling the super class constructor
        super().__init__(dog_name, dog_colour)

    def bark(self):
        print("Woof woof")


    def __str__(self):
        return "Woof! My name is " + self._name

