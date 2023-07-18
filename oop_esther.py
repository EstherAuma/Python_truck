"""
Assignment;
-Create ten classes each atleast with corresponding five objects,
out of the classes, print once for each object.
"""


class Cloth: #First class
    name = "skirts"
    color = "Black"
    size = "Small"

print(f"I love {Cloth.color} {Cloth.name}. ")

cloth2 = Cloth()
name = "Dresses"
color = "Pink"
size = "Medium"
print(f"I love {cloth2.color} {cloth2.name}. ")


cloth3 = Cloth()
name = "T-shits"
color = "White"
size = "Small"
print(f"I love {cloth3.color} {cloth3.name}. ")


cloth4 = Cloth()
name = "Trousers"
color = "Black"
size = "Medium"
print(f"I love {cloth4.color} {cloth4.name}. ")

cloth5 = Cloth()
cloth5.name = "Blouses"
cloth5.color = "Pink"
cloth5.size = "Small"
print(f"I love {cloth5.color} {cloth5.name}. ")


class Disease: #Second class
    name = "Malaria"
    sign = "Severe coldness"
    cause = "Plasmoduim"
print(f"{Disease.name} is caused by {Disease.cause}.")

disease2 = Disease()
disease2.name = "cough"
disease2.sign = "itching of the throat"
disease2.cause = "bacteria"
print(f"{disease2.name} is caused by {disease2.cause}.")


disease3 = Disease()
disease3.name = "HIV"
disease3.sign = "Low resistance to other diseases"
disease3.cause = "virus"
print(f"{disease3.name} is caused by {disease3.cause}.")


disease4 = Disease()
disease4.name = "Trachoma"
disease4.sign = "Itching of the eyes"
disease4.cause = "Bacteria"
print(f"{disease4.name} is  caused by{disease4.cause}")

disease4 = Disease()
disease4.name = "Diorrhoea"
disease4.sign = "Running stomach"
disease4.cause = "Bacteria"
print(f"{disease4.sign} is a sign of {disease4.name}")

class Artist: #Third class
    name = "Ada Ehi"
    sex = "Female"
    song = "Gospel songs"
print(f"{Artist.name} sings only {Artist.song}")

artist2 = Artist()
artist2.name = "Izzy"
artist2.sex = "Male"
artist2.song = "worly songs"
print(f"{artist2.name} sings only {artist2.song}.")

artist3 = Artist()
artist3.name = "Molly Ocen"
artist3.sex = "female"
artist3.song = "gospel songs"
print(f"{artist3.name} is a {artist3.sex} gospel artist.")

artist4 = Artist()
artist4.name = "John Blaq"
artist4.sex = "male"
artist4.song = "worly songs"
print(f"{artist4.name} is an artist who sings  {artist4.song} only.")

artist5 = Artist()
artist5.name = "Sheeba"
artist5.sex = "female"
artist5.song = "worly songs"
print(f"{artist5.name} is a {artist5.sex} artist who sings  {artist5.song} only.")

class Bus: #Forth class
    name = "Link bus"
    color = "green"
    route_for_operation = "Kampala-Gulu highway"
print(f"{Bus.name} operates along {Bus.route_for_operation}.")

bus1 = Bus()
bus1.name = "Acanadiro bus"
bus1.color = "white"
bus1.route_for_operation = "Kampala-Lira highway"
print(f"{bus1.name} operates along {bus1.route_for_operation}.")

bus2 = Bus()
bus2.name = "Friendship bus"
bus2.color = "blue"
bus2.route_for_operation = "Kampala-Gulu highway"
print(f"{bus2.name}  is {bus2.color} in color and operates along {bus2.route_for_operation}.")

bus3 = Bus()
bus3.name = "Makome bus"
bus3.color = "green"
bus3.route_for_operation = "Kampala-Gulu highway"
print(f"{bus3.name} operates along {bus3.route_for_operation}.")

bus4 = Bus()
bus4.name = "Gagga bus"
bus4.color = "white"
bus4.route_for_operation = "Kampala-Gulu highway"
print(f"{bus4.name} operates along {bus4.route_for_operation}.")

class Insect: #Fifth class
    name = "housefly"
    number_of_legs = 6
    metamorphosis = "complete"
print(f" A {Insect.name} undergoes {Insect.metamorphosis} metamorphosis. ")

insect2 = Insect()
insect2.name = "cockroach"
insect2.number_of_legs = 6
insect2.metamorphosis = "incomplete"
print(f" A {insect2.name} undergoes {insect2.metamorphosis} metamorphosis. ")

insect3 = Insect()
insect3.name = "butterfly"
insect3.number_of_legs = 6
insect3.metamorphosis = "complete"
print(f" A {insect3.name} undergoes {insect3.metamorphosis} metamorphosis. ")

insect4 = Insect()
insect4.name = "grasshopper"
insect4.number_of_legs = 6
insect4.metamorphosis = "incomplete"
print(f" A {insect4.name} undergoes {insect4.metamorphosis} metamorphosis. ")

insect5 = Insect()
insect5.name = "mosquito"
insect5.number_of_legs = 6
insect5.metamorphosis = "complete"
print(f" A {insect5.name} undergoes {insect5.metamorphosis} metamorphosis. ")

class River: #Sixth class
    name = "R.Nile"
    length = "very long"
print(f"{River.name} is {River.length}.")

river2 = River()
river2.name = "R.Congo"
river2.length = "long"
print(f"{river2.name} is {river2.length}.")

river3 = River()
river3.name = "R.Kafu"
river3.length = "short"
print(f"{river3.name} is {river3.length}.")

river4 = River()
river4.name = "R.Limpopo"
river4.length = "very long"
print(f"{river4.name} is {river4.length}.")

river5 = River()
river5.name = "Orange river"
river5.length = "very long"
print(f"{river5.name} is {river5.length}.")

class Moutain: #Seventh class
    name = "mt.Rwenzori"
    country = "Uganda"
print(f"{Moutain.name} is located in {Moutain.country}.")

mountain2 = Moutain()
mountain2.name = "mt.Elgon"
mountain2.country = "Uganda"
print(f"{mountain2.name} is located in {mountain2.country}.")

mountain3 = Moutain()
mountain3.name = "mt.Kilimanjaro"
mountain3.country = "Tanzania"
print(f"{mountain3.name} is located in {mountain3.country}.")

mountain4 = Moutain()
mountain4.name = "mt.Kenya"
mountain4.country = "Kenya"
print(f"{mountain4.name} is located in {mountain4.country}.")

mountain5 = Moutain()
mountain5.name = "mt.Mufumbiro"
mountain5.country = "Uganda"
print(f"{mountain5.name} is located in {mountain5.country}.")

class University: #Eigth class
    name = "Gulu university"
    district_located = "Gulu"
print(f" I would like to study from {University.name}.")

university2 = University()
university2.name = "Mbarara university"
university2.district_located = "Mbarara"
print(f"{university2.name} is located in {university2.district_located} district.")

university3 = University()
university3.name = "Lira university"
university3.district_located = "Lira"
print(f"{university3.name} is located in {university3.district_located} district.")

university4 = University()
university4.name = "Kabale university"
university4.district_located = "Kabale"
print(f"{university4.name} is located in {university4.district_located} district.")

university5 = University()
university5.name = "Kyambogo university"
university5.district_located = "Kampala"
print(f"{university5.name} is located in {university5.district_located} district.")

class Bird: #Ninth class
    name = "Chiken"
    type = "domestic"
print(f"{Bird.name} is a {Bird.type} bird.")

bird2 = Bird()
bird2.name = "ostrich"
bird2.type = "wild"
print(f" An {bird2.name} is a {bird2.type} bird.")

bird3 = Bird()
bird3.name = "turkey"
bird3.type = "domestic"
print(f" A {bird3.name} is a {bird3.type} bird.")

bird4 = Bird()
bird4.name = "guinea fowl"
bird4.type = "domestic"
print(f" A {bird4.name} is a {bird4.type} bird.")

bird5 = Bird()
bird5.name = "dove"
bird5.type = "domestic"
print(f" A {bird5.name} is a {bird5.type} bird.")

class Crop: #Tenth class
    name = "Maize"
    classification = "monocotyledonous"
print(f"{Crop.name} is classified as a {Crop.classification} plant.")

crop2 = Crop()
crop2.name = "Beans"
crop2.classification = "dicotyledonous"
print(f"{crop2.name} are classified as  {crop2.classification} plants.")

crop3 = Crop()
crop3.name = "Millets"
crop3.classification = "monocotyledonous"
print(f"{crop3.name} are classified as  {crop3.classification} plants.")

crop4 = Crop()
crop4.name = "sorghum"
crop4.classification = "monocotyledonous"
print(f"A {crop4.name} is classified as a  {crop4.classification} plants.")

crop5 = Crop()
crop5.name = "Pease"
crop5.classification = "dicotyledonous"
print(f" {crop5.name} are classified as {crop5.classification} plants.")