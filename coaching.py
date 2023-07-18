students = []
def register():
    name1 = input("please enter your name here: ")
    room = input("please enter your class here: ")
    
    students.append(name1)
    students.append(room)
    print(students)
   

r=0
while r<3:#How to evoke the function three times
    register()
    r+=1

r = 0
for r in range(1):#for loop is used to iterate items in a list.
    if len(students) >= 1:
        print("we have registered students.")
    elif len(students) <1:
        print("There are no students registered.")
        register()

