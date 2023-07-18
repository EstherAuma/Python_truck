 if len(students) == 0:
        print("No students registered yet.")
    else:
        for student in students:
            print("First Name:", student["First Name"])
            print("Last Name:", student["Last Name"])
            print("Date of Birth:", student["Date of Birth"])
            print("Class Registering For:", student["Class Registering For"])
            print("Location:", student["Location"])
            print("Parent's Name:", student["Parent's Name"])
            print("Payment Status:", student["Payment Status"])
            print("------------------------")
