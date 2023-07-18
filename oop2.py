'''
ABSTRACTION
Variables are refered to as properties, artributes or x-tics
Class is also a block of code.
Class name begins with a capital letter.
For this case, variables are now termed as a properties.
-Method does not change for every objects of a class.
'''
class Girl:
    name = "Savior"
    age = 2
    gender = "female"
    size_of_bra = "small"
    family = "God's grace family"
    size = "small"
    def greet():
        print("Hello world!")
        return "I love my people"
Girl.greet()#prints the function without a return statement.
print(Girl.greet())# helps to print out what is written in the return statement
print(Girl.name)#(.) operator is used to access the value of a class

girl2 = Girl()
girl2.name = "Esther"
girl2.age = 45
girl2.gender = "Female"

print(f"{girl2.name} is {girl2.age} years old")#f stand for format


girl3 = Girl()
girl3.name = "Monica"
girl3.age = 20
girl3.gender = "female"

'''
All those is how to create a class in python
Assinment; create atleast 10 classes each with  corresponding 5 objects, out of the classes print once for each object
'''