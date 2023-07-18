"""
Assignment;
-Use constructors to create ten classes each with five objects.
"""

#Define a class called Teacher
class Teacher:
    '''
    -Constructer to initialise name, age, class taught by the teacher, 
    subject taught by the teacher and the teacher's salary.
    '''
    def __init__(self,name,age, class_taught, subject, salary):
        self.name = name
        self.age = age
        self.class_taught = class_taught
        self.subject = subject
        self.salary = salary
        #Method to print details of the teacher
    def details(self):
        print(f"{self.subject} is taught by {self.name}.")
#Instances of a class 'Teacher'
teacher1 =Teacher("Sarah",24,"form six","Literature",700000,)
teacher1.details()

teacher2 = Teacher("Monica",20, "form two","English", 500000)
teacher2.details()

teacher3 = Teacher("Esther",45, "form five","Biology", 800000)
teacher3.details()

teacher4 = Teacher("Mike",30, "form one","CRE", 500000)
teacher4.details()

teacher4 = Teacher("Francis",40, "form six","Chemistry", 1000000)
teacher4.details()

#Define a class 'University'
class University:
    '''
    -Constructor to initialize university's name, number of students
    number of lecturers and location of a university
    '''
    def __init__(self, name, num_students, num_lecturers, location):
        self.name = name
        self.num_students = num_students
        self.num_lecturers = num_lecturers
        self.location = location

        #Method to print the statement about the university
    def statement(self):
        print(f"{self.name} is located in {self.location}")

#Instances of the class 'University'
university1 = University("Kyambogo University",40000,200,"Kampala.")
university1.statement()

university2 = University("Makerere University",50000,300,"Kampala.")
university2.statement()

university3 = University("Gulu University",3000,200,"Gulu district.")
university3.statement()

university4 = University("Mbarara University",10000,400,"Mbarara district.")
university4.statement()

university5 = University("Lira University",5000,400,"Lira district.")
university5.statement() 

#Define a class 'Occupation'
class Occupation:
    '''
    -Constructer to initialize name, qualification and salary of
    the occupation
    '''
    def __init__(self, name,qualification,salary):
        self.name = name
        self.qualification = qualification
        self.salary = salary
    
    #Method print the identity of the occupation
    def identify(self):
        print(f"{self.name} needs {self.qualification} as a qualification.")

#Instances of the class 'Occupation'
occupation1 = Occupation("Teaching","bachelor",50000)
occupation1.identify()

occupation2 = Occupation("Law","bachelor",1000000)
occupation2.identify()

occupation3 = Occupation("Engineering","bachelor",14000000)
occupation3.identify()       
        
occupation4 = Occupation("Nursing","diploma",500000)
occupation4.identify()

occupation5 = Occupation("Accounting","diploma",60000)
occupation5.identify()

#Define a class 'Denomination'
class Denomination:
    '''
    -Constructor to initialize name, holy book, prayer day and worship place
    for the denomination
    '''
    def __init__(self,name,holy_book,prayer_day,worship_place):
        self.name = name
        self.holy_book = holy_book
        self.prayer_day = prayer_day
        self.worship_place = worship_place
    #Method to print details of the denomination
    def details(self):
        print(f"{self.name} pray on {self.prayer_day}")
#Instances of the class 'Denomination'
denomination1 = Denomination("Anglicans","Bible","Sunday.","Church")
denomination1.details()

denomination2 = Denomination("Catholics","Bible","Sunday.","Church")
denomination2.details()

denomination3 = Denomination("Islams","Quoran","Friday.","Mosque")
denomination3.details()

denomination4 = Denomination("PAG","Bible","Sunday.","Church")
denomination4.details()

denomination5 = Denomination("SDA","Bible","Sunday.","Church")
denomination5.details()

#Define a class 'Disease'
class Disease:
    '''
    -Constructor to initialize name, cause,symptom
    and prevention of the disease
    '''
    def __init__(self,name,cause,symptom,prevention):
        self.name =name
        self.cause = cause
        self.symptom = symptom
        self.prevention = prevention

    #Method to print details of the disease
    def details(self):
        print(f"{self.name} is caused by {self.cause}.")

#Instances of a class 'Disease'
disease1 = Disease("Malaria","plasmodium parasites.","nausea and vomiting"," take antimalarial medication")
disease1.details()

disease2 = Disease("Typhoid","bacteria.","high fever","vaccination")
disease2.details()

disease3 = Disease("Whooping cough","bacteria.","nasal congestion","vaccination")
disease3.details()

disease4 = Disease("Dsentery","bacteria.","crams","drink clean water")
disease4.details()

disease5 = Disease("Measles","measles virus.","sore throat","vaccination")
disease5.details()


#Dfine a class 'Mountain'
class Mountain:

    '''
    -Constructer to initialize name, type 
    and location of the mountain
    '''
    def __init__(self,name,type,location,):
        self.name =name
        self.type = type
        self.location = location
    
    #Method to print details of the mountain
    def details(self):
        print(f"{self.name} is formed by {self.type}.")

#Instances of the class 'Mountain'
mountain1 = Mountain("Mt.Elgon","volcanic eruption","Tororo district")
mountain1.details()

mountain2 = Mountain("Mt.Kenya","volcanic eruption","Central Kenya")
mountain2.details()

mountain3 = Mountain("Mt.Kilimanjaro","volcanic eruption","Tanzania")
mountain3.details()

mountain4 = Mountain("Mt.Mufumbiro","volcanic eruption","Kiso district")
mountain4.details()

mountain5 = Mountain("Mt.Rwenzori","volcanic eruption","Kasese district")
mountain5.details()

#Define a class 'Food'
class Food:

    '''
    -Constructor to initialize name, nutrients and
    price per kilo of the food
    '''
    def __init__(self,name,nutrient,price_per_kilo,):
        self.name =name
        self.nutrient = nutrient
        self.price_per_kilo = price_per_kilo

    #Mothod to print amounts of the food
    def amounts(self):
        print(f"{self.name} is sold at {self.price_per_kilo} a per kilo.")

#Instances of the class 'Food'
food1 = Food("Rice","carbohydrates",40000)
food1.amounts()

food2 = Food("Posho","carbohydrates",3000)
food2.amounts()

food3 = Food("Meat","proteins",15000)
food3.amounts()

food4 = Food("Beans","proteins",5000)
food4.amounts()

food5 = Food("Pease","proteins",3000)
food5.amounts()


#define a clss 'Hospital'
class Hospital:

    '''
    -Constructor to initialize name, location and
    number of patients in a hospital
    '''
    def __init__(self,name,location,num_patients,):
        self.name =name
        self.location = location
        self.num_patients = num_patients

    #Method to print details of the hospital
    def details(self):
        print(f"{self.name} is located in  {self.location}.")

#Instances of the class hopital
hospital1 = Hospital("Mulago hospital","Kampala",100000)
mountain1.details()

hospital2 = Hospital("Gulu RR hospital","Gulu district",50000)
hospital2.details()

hospital3 = Hospital("Lira RR hospital","Lira district",1000)
hospital3.details()

hospital4 = Hospital("St.Mary's Lacho hospital","Gulu district",5000)
hospital4.details()

#Define a class 'Artist'
class Artist:

    '''
    -Constructor to initialize name, age,song
    and coutry of the artist
    '''
    def __init__(self,name,age,song,country):
        self.name =name
        self.age = age
        self.song = song
        self.country = country
    
    #Method to print the status of the artist
    def status(self):
        print(f"{self.name} comes from  {self.country}.")


#Instances of the class 'Artist'
artist1 = Artist("Ada Ehi",30,"gospel songs","Nigeria")
artist1.status()

artist2 = Artist("Azawi",32,"worldly songs","Uganda")
artist2.status()

artist3 = Artist("Mercy Chinwo",21,"gospel songs","Nigeria")
artist3.status()

artist4 = Artist("Vinka",28,"worldly songs","Uganda")
artist4.status()

artist5 = Artist("Kenzo",28,"worldly songs","Uganda")
artist5.status()


#Define a class 'Crop'
class Crop:

    '''
    -Constructor to initialize name, classification and 
    type of the crop
    '''
    def __init__(self,name,classification,type):
        self.name =name
        self.classification = classification
        self.type = type
    
    #Method to print details of the crop
    def details(self):
        print(f"{self.name} is a {self.type} crop.")

#Instances of the class 'Crop'
crop1 = Crop("Beans","dicotyledonous","seasonal")
mountain1.details()

crop2 = Crop("Millet","monocotyledonous","seasonal")
crop2.details()

crop3 = Crop("Sorghum","monocotyledonous","seasonal")
crop3.details()

crop4 = Crop("Maize","monocotyledonous","seasonal")
crop4.details()

crop5 = Crop("Groundnuts","dicotyledonous","seasonal")
crop4.details()