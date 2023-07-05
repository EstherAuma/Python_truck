#Is an istruction that will tell a comp to repeatedly do something.

def count():
    for number in range(10):
        print(number)
count()
#accessing list elements using a loop
def example2():
    languages = ["python","javascript","c++","c#",]
    for language in languages:
        print(language)
example2()

def example3(num):
    for number in range(num):
        print(number)
example3(10)

def myLang():
    languages = ["python","javascript","c++","c#",]
    for language in languages:
        if language == "python":
            print("you are currently in python class")
myLang()

def even(num):
    for number in range(num):
        if number % 2 == 0:
            print(number)
even(10)

def odd(num):
    for number in range(num):
        if number % 2 != 0:
            print(number)
odd(10)

def power(p):
    my_po = p**2
    if my_po % 2 == 0:
        print("The power is an even number")
    else:
        print("the power is an odd number")

