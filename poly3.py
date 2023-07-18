# Define a class 'Cat' to represent a cat object
class Cat:
    # Constructor to initialize the cat's name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to print information about the cat
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    # Method to make the cat sound
    def make_sound(self):
        print("Meow")

# Define a class 'Dog' to represent a dog object
class Dog:
    # Constructor to initialize the dog's name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to print information about the dog
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    # Method to make the dog sound
    def make_sound(self):
        print("Bark")

# Create an instance of 'Cat' with name 'Kitty' and age '2.5'
cat1 = Cat("Kitty", 2.5)

# Create an instance of 'Dog' with name 'Fluffy' and age '4'
dog1 = Dog("Fluffy", 4)

# Iterate through the objects 'cat1' and 'dog1' using a for loop
for animal in (cat1, dog1):
    # Call the 'make_sound' method for the current animal 
    animal.make_sound()

    # Call the 'info' method to print information about the current animal
    animal.info()

    # Call the 'make_sound' method again for the current animal
    # This will print the sound again after the information is displayed
    animal.make_sound()
