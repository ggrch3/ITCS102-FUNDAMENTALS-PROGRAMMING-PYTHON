import os, time


print("STUDENT INFORMATION SYSTEM")
print(";===================================================;")

student_records = {}

while True: 
    print("Select from the options: \nA - Add Information\nB - Search a Record\nC - Delete a Record\nD - Modify a Record\nE - Exit\nP - Print All ")
    choice = input("Your Choice - - - - > ").lower()

    if choice == 'a':
        print("ADDING STUDENT INFORMATION")
        print(";=========================;")
        time.sleep(2)
        
        search_code = input("Key code - - - > ").upper()
        first_name = input("Enter First name - - > ").upper()
        last_name = input("Enter Last name - - - > ").upper()
        course = input("Enter Course - - - > ").upper()
        email = input("Enter email address - - - > ")

        student_records = {search_code : [first_name, last_name, course, email]}
        print("DATA SAVED")
        time.sleep(2)
        os.system('cls')
        continue

    elif choice == 'b':
        os.system('cls')
        code = input("Enter key code:  ")
        
        for j in student_records.keys():
            if code in student_records.keys():
                print("Record Found . . . ")
                time.sleep(2)
                
                for i in student_records[code]:
                    print(i)

            else: print("NO RECORD FOUND . . . ")
            time.sleep(2)
        continue
    elif choice =='c':
        pass
        continue
    elif choice == 'd':
        os.system('cls')
        print("MODIFYING . . . ")
        print(";===============;")
        
        code = input("Enter the key code of the data you want to modify: ")
        
        if code in student_records:
            print("Re-enter complete information:")
            fname = input("New First Name: ")
            lname = input("New Last Name: ")
            course = input("New Course: ")
            email = input("New Email: ")
        continue
    elif choice == 'e':
        print("END SYSTEM")
        break
    elif choice == "P":
        for i,j in student_records.items():
            print(f"Code - {i} INFO SAVED - - - > {j}")
    else:
        print("WRONG CHOICE")
        continue
    
    