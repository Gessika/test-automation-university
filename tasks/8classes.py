#Classes (= OBJECT) allows group data&information: variables and functions
# in a single organized unit
#allows to share info with other classes or with other parts of the program
'''
inheritance: child can use attributes&methods of parent class
multiple inheritance: child inherit attributes&methods from more then one class
polymorphysm: child can ovveride parent's methods
'''
import random

'''
class variable: for use inside a class;
instance variable (екземпляр): for use by specific method in whoch created/declared
'''
# __init__ allows every instance of a class to be created with specific parameter|
# Used to set defaul state of object when created
# init Has paraneters that accept arguments which determine the attributes of the object
# __self__ allows info to be shared easilly and efficiently
# represents instance of class, DO available all attributes through a class.
# If method is running as a part of a class, rather as a instanse of a class -> then its not needed

# Attributes - characteristics that every object can have
class Person:
    def __init__(self, firstname, lastname, health, status):
        self.firstname = firstname  # allows us to make characteristics available
        self.lastname = lastname    #  in our init method, or in the other methods
        self.health = health
        self.status = status

    def introduce(self):
        print(f"Hi, I'm {self.firstname} {self.lastname}")

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print(f"{self.firstname} is happy today")
        elif emotion == 2:
            print(f"{self.firstname} is sad right now")

    def status_change(self):
        if self.health == 100:
            print(f"{self.firstname} is totally healthy")
        elif self.health >= 76:
            print(f"{self.firstname} is a bit tired now")
        elif self.health >= 51:
            print(f"{self.firstname} feels unwell")
        elif self.health >= 40:
            print(f"{self.firstname} goes to the doctor")
        else:
            print(f"{self.firstname} is unconscious.")

Maria = Person("Masha", "Giu", 95, status ="True")
Rey = Person("Rey", "Smith", 88, status ="False")
Lee = Person("Lee", "Smith", 72, status ="True")

print(f"{Maria.firstname} is my friend? {Maria.status}")
print(f"{Rey.firstname} is my friend? {Rey.status}")

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()

Maria.emote()