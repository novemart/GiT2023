from animal import Animal

#inheritance
class Cat(Animal):

    # class variable
    # accessible directly through the class name
    number_of_cats = 0

    # constructor
    def __init__(self, cat_name, cat_colour):
        # instance variable, attribute called _name
        # self._name = cat_name
        # calling the super class constructor
        super().__init__(cat_name, cat_colour)
        #self._colour = cat_colour
        # using the class variable
        Cat.number_of_cats += 1

    # method; self parameter is required
    def purr(self):
        print("Purr purr")

    # method accepting one extra parameter
    def hunt(self, thing):
        print("Yum yum, I'm hunting a ", thing)


    # overriding
    # changing the functionality declared in the parent class
    def make_sound(self):
        return "Meow meow"

    # getter
    def get_name(self):
        return(self._name + " is " + self._colour)

    # setter
    def set_height(self, cat_height):
        self._height = cat_height

    # method to change the cat's name
    def set_name(self, newName):
        self._name = newName