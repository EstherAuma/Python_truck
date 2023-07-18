"""
HOW THE DYNAMIC CLASSES OPERATES
-we have static classes and dynamic classes
"""
class School:
   def   __init__(self, name, motto, location, no_teachers, no_students): #is a special method that helps us to pass value of properties of the objects.
    self.name = name# self is a reference that denotes the property of a school.
    self.motto = motto
    self.location = location
    self.no_teachers = no_teachers
    self.no_students = no_students
   def register(self):#method 'register'  is overloaded coz different objects uses it differently.
       print(f"{self.name} is fully registered with UNEB")

#the function is making the class dynamic
school1 = School("Light Voc.","Success throught persistance","Lira",30,3000)
school1.register()

school2 = School("St.John's colege","In Gog we Trust","Mpigi",24,2000)
school2.register()

'''
-A method of a class is called a constructor.
-A constructor is used to initialise an instantiated object.
-Here the first school(first object) has been instantiated.
-Instantiation is the process of creating objects of a class.

'''
class Country:
  def __init__(self,A,B,C):#self denotes the property
    self.name = A
    self.city = B
    self.population = C

country1 = Country("Uganda","Kampala",200000.)
#in the programming worl, people prefer using self
#init functionis sometimes is called the shis


class Continent:
  def __init__(continent, a, b, c):#The first parameter is arefernce to the property of the object.
    continent.name = a
    continent.lakes = b
    continent.river = c




