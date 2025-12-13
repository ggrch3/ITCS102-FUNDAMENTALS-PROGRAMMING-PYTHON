

import time
# 1. Content from activity10.py (Basic if/else Discount Logic)
def demo_student_discount():
    print("Conditional Demo 1: Student Discount Check")
    
    name = input("Insert your name --> ")
    IsStudent = input("Are you a student (Yes/No) --> ").lower()
    try:
        fare = eval(input("Enter payment amount -> "))
    except (NameError, TypeError):
        print("Invalid fare input. Assuming fare is 100 for demo.")
        fare = 100

    print("\nVerifying if student status...")
    time.sleep(1)

    if IsStudent == "yes":
        discount = fare * 0.2
        new_fare = fare - discount
        print("Hi", name, "Verification finished ✓")
        time.sleep(1)
        print(f"Discount applied. New fare is: {new_fare}")
    else:
        print("There seems to have a problem.")
        time.sleep(0.5)
        print("It seems that you are not a student.", name, "No discount applied.")
        time.sleep(0.5)
        print(f"Fare is: {fare}")
    print("=" * 40)

# 2. Content from activity11.py (Complex if/elif/else Temperature Logic)
def demo_temperature_logic():
    print("Conditional Demo 2: Temperature Logic Check")
    try:
        temp = eval(input("Enter Temperature --> "))
    except (NameError, TypeError):
        print("Invalid temperature input. Assuming temp is 25 for demo.")
        temp = 25

    if temp <= -51:
        print("It's the ice age all over again")
    elif temp >= -50 and temp <= -1:
        print("The Temperature is Too Cold")
    elif temp >= 1 and temp <= 20:
        print("The Temperature is Cold")
    elif temp >= 21 and temp <= 30:
        print("The Temperature is LukeWarm")
    elif temp >= 31 and temp <= 40:
        print("The Temperature is Warm")
    elif temp >= 41 and temp <= 50:
        print("The Temperature is Latina type")
    elif temp >= 51:
        print("you're cooked gng")
    else:
        print("Don't touch the thermostat if you ain't doing it right.")
    print("=" * 40)

# 3. Content from code_challange3.py (Login with Logical Operator 'and')
def demo_simple_login():
    print("Conditional Demo 3: Simple Login System")
    
    correct_username = "ggrch3"
    correct_password = "hakdog123"
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if password == correct_password and username == correct_username:
        print("ACCESS GRANTED.")
        time.sleep(1)
        print("Welcome you scum.")
    else:
        print("You are not the person you used to be.")
        time.sleep(1)
        print("Scum. Access Denied.")
    print("=" * 40)

# 4. Content from code_challange4.py (Even/Odd Check with Modulus)
def demo_even_odd_check():
    print("Conditional Demo 4: Even/Odd Check")
    try:
        number = eval(input("Enter number --> "))
    except (NameError, TypeError):
        print("Invalid input. Assuming number is 10 for demo.")
        number = 10
        
    if number % 2 == 0:
        print(f"{number} is EVEN")
    else:
        print(f"{number} is ODD")
    print("=" * 40)

# 5. Content from code_challange5.py (Manga Recommender)
#(if/elif/else).
def demo_manga_recommender():
    
    print("Conditional Demo 5: Manga Recommender (Complex if/elif)")
    print("Answer some questions to get a recommendation.")

    genre = input("What genre would you like (action, romance, ecchi): ").lower()
    duration = input("How long (short, medium, long): ").lower()
    decade = input("In what decade (90s, 2000s, 2010s, 2020s): ").lower()

    time.sleep(1)
    print("\nProcessing recommendations...")
    time.sleep(1)

    if genre == "action" and duration == "short" and decade == "90s":
        print("Recommendation: Basara, Battle Angel Alita, Gunsmith cats.")
    elif genre == "action" and duration == "long" and decade == "90s":
        print("Recommendation: One Piece, Berserk, Dragon Ball, SLam Dunk.")
    elif genre == "ecchi" and duration == "long" and decade == "2010s":
        print("Recommendation: Food Wars!, TR.")
    else:
        print("No exact match found for your criteria. Try different combinations.")
    print("=" * 40)

# MASTER FUNCTION: Run all demos for the main menu Topic 4 selection
def run_topic_4_all():
    print("\n" + "="*50)
    print("TOPIC 4: CONDITIONAL STATEMENTS DEMONSTRATION")
    print("="*50)
    
    demo_student_discount()
    demo_temperature_logic()
    demo_simple_login()
    demo_even_odd_check()
    demo_manga_recommender()
    
    print("\n" + "="*50)
    print("All Conditional (if/elif/else) types demonstrated.")
    print("="*50)


def check_even_odd(number):
    if number % 2 == 0:
        return "EVEN"
    else:
        return "ODD"