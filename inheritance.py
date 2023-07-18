"""
INHERITANCE
-The piece of code below demonstrates inheritance where
class dog and snake are taking properties of class Animal.
_ The class Dog and Snake are not relatable to one another 
but are related to the class Animal.
_Dog has inherited all the artributes of a class Animal.
-changing the value of a property you have inherited is called overiding. 
"""


class Animal:
    name = ""
    family =""
    gender ="" 

class Dog(Animal):#Here we have inherited the class animal by the class Dog. 
    sound = "bark"
    def investigate(self):
        print(f"{self.name} investigates by sniffing")

class Snake(Animal):
    sound = "hishing"
    def investigate(self):
        print(f"{self.name} move by crowling")

#Let's instantiate the objects of a class dog.
jsp = Dog()
jsp.name = "Rock"
jsp.family = "dog"
jsp.gender = "male"
print(f"{jsp.sound}")



#An instance of a class Snake
snake1 = Snake()
snake1.name = "python"
snake1.family = "reptiles"
snake1.gender = "female"
print(f"{snake1.sound}")







