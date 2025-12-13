
import time
import os


# FUNCTION DEMONSTRATIONS (from activity24.py)


def greeter(name):
    print(f"Hello {name}, welcome to the Modular World!")
    
def summation(x):
    total = 0
    for y in range(x, 0, -1):
        total += y
    print(f"The sum of all numbers from {x} down to 1 is: {total}")

def demo_functions():
    print("Function Demo 1: Basic Greeter")
    greeter("Geroche")
    greeter("Paul")

    print("\nFunction Demo 2: Summation Function")
    try:
        num = int(input("Enter a number to calculate its full summation: "))
        summation(num)
    except ValueError:
        print("Invalid input for summation. Skipping.")
    print("=" * 40)


# DICTIONARY DEMONSTRATIONS (from activity26.py and activity27.py)


def demo_basic_dictionary():
    print("Dictionary Demo 1: Key-Value Access")
    pl = {'Mine':'craft', 'smash':'bros', 'devil':'may cry'}
    
    print(f"Dictionary content: {pl}")
    print(f"Accessing value of key 'Mine': {pl['Mine']}")
    
    pl['final'] = 'fantasy'
    print(f"After adding 'final':'fantasy': {pl}")
    print("=" * 40)

def demo_interactive_dictionary():
    print("Dictionary Demo 2: Interactive Anime Database")
    empty_dictionary = {}
    
    def print_anime():
        print("\nCurrent Anime List")
        if not empty_dictionary:
            print("List is empty.")
            return
        for i, j in empty_dictionary.items():
            print(f"Key: {i} | Title: {j}")
        print("--------------------------")

    def search_anime(key):
        print("Searching anime in dictionary...")
        if key in empty_dictionary:
            print(f"RESULT FOUND: Key '{key}' corresponds to title: {empty_dictionary[key]}")
        else:
            print(f"Anime with key '{key}' not found.")
    
    while True:
        keys = input("Enter unique key for this anime (e.g., A001)> ").upper()
        value = input("Enter the anime title> ").upper()

        empty_dictionary[keys] = value
        print(f"Data saved: {keys} - {value}")
        
        choice = input("\nOptions: Y=Continue adding | N=Exit | P=Print list | S=Search list> ").lower()

        if choice == 'n':
            break
        elif choice == "p":
            print_anime()
            continue
        elif choice == "s":
            search = input("Enter the key to search for: ").upper()
            search_anime(search)
            continue
        elif choice == 'y':
            continue
        else:
            print("Invalid input, defaulting to continue adding.")
            continue
    print("Interactive Dictionary Demo Finished.")
    print("=" * 40)



# CHALLENGE: STUDENT INFORMATION SYSTEM (From code_challange16.py)


def demo_student_info_system():
    print("CHALLENGE: Student Information System (CRUD Demo)")
    student_records = {}

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def add_record():
        clear_screen()
        print("ADDING STUDENT INFORMATION")
        search_code = input("Key code (e.g., ID#) --> ").upper()
        first_name = input("First Name: ").upper()
        last_name = input("Last Name: ").upper()
        course = input("Course: ").upper()
        email = input("Email: ")
        
        student_records[search_code] = [first_name, last_name, course, email]
        print("\nDATA SAVED.")
        time.sleep(1)

    def search_record():
        clear_screen()
        print("SEARCH A RECORD")
        code = input("Enter key code: ")
        
        if code in student_records:
            print("\nRecord Found:")
            data = student_records[code]
            print(f"ID: {code}")
            print(f"Name: {data[0]} {data[1]}")
            print(f"Course: {data[2]}")
            print(f"Email: {data[3]}")
        else:
            print("NO RECORD FOUND.")
        time.sleep(2)

    def print_all_records():
        clear_screen()
        print("ALL STUDENT RECORDS")
        if not student_records:
            print("No records stored.")
            time.sleep(1)
            return

        for code, data in student_records.items():
            print(f"\nID: {code}")
            print(f"Name: {data[0]} {data[1]}")
            print(f"Course: {data[2]}")
            print(f"Email: {data[3]}")
            print("-" * 15)
        input("Press Enter to continue...")

    while True: 
        clear_screen()
        print("STUDENT INFORMATION SYSTEM (CRUD)")
        print("="*40)
        print("A - Add Information\nB - Search a Record\nP - Print All\nE - Exit")
        choice = input("Your Choice: ").lower()

        if choice == 'a':
            add_record()
        elif choice == 'b':
            search_record()
        elif choice == 'p':
            print_all_records()
        elif choice == 'e':
            print("System terminated.")
            break
        else:
            print("Invalid selection. Try again.")
            time.sleep(1)
    print("=" * 40)

def run_topic_7_all():
    print("\n" + "="*50)
    print("TOPIC 7: FUNCTIONS & DICTIONARIES DEMONSTRATION")
    print("="*50)
    
    demo_functions()
    demo_basic_dictionary()
    demo_interactive_dictionary()
    demo_student_info_system()
    
    print("\n" + "="*50)
    print("All Functions and Dictionaries demonstrated.")
    print("="*50)


def generate_greeting(name):
    greeting = f"Hello, {name}! This greeting was generated by a modular function."
    return greeting