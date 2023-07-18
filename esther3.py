students = []  # List to store registered students

def register_student():
    print("Welcome to Aunt Esther nursery school")
    print("New Student Registration")
    print("------------------------")
    first_name = raw_input("Enter student's first name: ")
    last_name = raw_input("Enter student's last name: ")
    date_of_birth = input("Enter student's date of birth (DD/MM/YYYY): ")
    class_registering_for =raw_input("Enter class registering for: ")
    location = raw_input("Enter location: ")
    parent_name = raw_input("Enter parent's name: ")
    payment_status = raw_input("Has the payment been made? (yes/no): ")
    print("Every student should pay Shs.500000")

    student = {
        "First Name": first_name,
        "Last Name": last_name,
        "Date of Birth": date_of_birth,
        "Class Registering For": class_registering_for,
        "Location": location,
        "Parent's Name": parent_name,
        "Payment Status": payment_status,
        
    }

    students.append(student)  # Append the student to the list of students
    print("Registration successful!\n")

register_student()


def display_registered_students():
    print("Summary of Registered Students")
    print("-------------------------------")
   
display_registered_students()



    
    
    