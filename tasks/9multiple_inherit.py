#parent class is used in a child class:

#Parent class 1
class Item():
    def __init__(self, artikul):
        self.artikut = artikul

    # creating one method inside of each class:
    def print_artikul(self):
        print(f"The artikul is {self.artikut}")

#Parent class 2
class Clothing():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    # creating one method inside of each class
    def print_clothing(self):
        print(f"The clother is in section {self.section} and {self.type} type")


#Child Class
class Shirts(Item, Clothing):
    def __init__(self, artikul, section, type, name, color):
        self.name = name
        self. color = color
        #initialize attributes from Parent's class:
        Item.__init__(self, artikul)
        Clothing.__init__(self, section, type)

    def print_shirts(self):
        print(f"the {self.name} in {self.color} color on sale!")

#making a class Child item:
Blouse = Shirts("001", 43, "Top", "Blouse", "white")
#calling Parent's methods:
Blouse.print_artikul()
Blouse.print_clothing()
Blouse.print_shirts()

'''
Polym: when we want to allow the child class to have a method with the same name
and similar implementation as a parent class 
and we wish for that methods to override the parent class method
'''






