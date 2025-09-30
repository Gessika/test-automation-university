# args and kwargs
'''
def user_info(name, age, city="kharkow"):
    print('{} is {} years old from {} city.'.format(name, age, city))

user_info('Ira', 38)
user_info("Micah")
user_info(age=56, name="Kadeem")
'''

# *args and **kwargs
def say_hello(name, company, email, *args, **kwargs):
    print("{} works at {}. Her email is {}.".format(name, company, email))

    #Виводимо *args
    if args:
        print("Additional positional info:", args)

    # Виводимо *args
    if kwargs:
        for key, value in kwargs.items():
            print("  {}: {}".format(key, value))

say_hello("Jess", "Ingrass", "mail @ mail.com",
           "Teach Code", 75000, hire_date = "September 2010")