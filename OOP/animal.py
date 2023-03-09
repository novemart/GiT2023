# super class
class Animal:

    # superclass consctructor
    def __init__(self, an_name, an_colour):
        self._name = an_name
        self._colour = an_colour

    def make_sound(self):
        return " "

    def sleep(self):
        print("ZZZZZZZZZZZZ")