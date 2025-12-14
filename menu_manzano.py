import time
import sys
import os
import print_statements
import variables_topic
import operators_topic
import conditionals_topic
import loops_topic
import lists_topic
import functions_topic

from print_statements import demo_print_triangle, demo_basic_print,demo_escape_characters
from variables_topic import demo_data_type, demo_input_greeting,demo_string_length
from operators_topic import demo_basic_arithmetic, demo_assignment_operators,demo_atm_denomination
from conditionals_topic import demo_student_discount, demo_temperature_logic,demo_simple_login, demo_even_odd_check, demo_manga_recommender
from loops_topic import demo_basic_for_loop, demo_repeat_sleep, demo_descending_countdown, demo_summation_input, demo_calculate_factorial,demo_multiplication_table, demo_rocket_countdown, demo_sum_odd_numbers,demo_simple_while_break, demo_guessing_game, demo_odd_number_collector, demo_basic_nested_loop, demo_star_triangle, demo_number_pyramid,demo_number_triangle, demo_right_aligned_star_triangle, demo_diamond_pattern,demo_composite_star_pattern
from lists_topic import demo_list_methods, demo_anime_list_builder
from functions_topic import demo_functions, demo_basic_dictionary, demo_interactive_dictionary, demo_student_info_system
# These imports are of use whenever a topic wants to call a demonstration.

# key difference that I just found out, 
# Import, imports the entire module
# from [name] import [thing] - it calls the function directly and is used for much smaller programs



def type_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pause_and_return():
    type_print("================================================", delay=0)
    input("Press ENTER to return to the Main Menu")
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# special effects, because I'm just that type of dud


# Title
print("================================================")
print("\tFinal Project : Python Fundamentals")
print("\tWelcome to Interactive menu program")
print("================================================")
time.sleep(3)
os.system('cls')



# Topic No. 1 Print Statements
def topic_print():
    clear_screen()
    while True:
        print("================================================")
        print("TOPIC 1: PRINT STATEMENTS SUB-MENU")
        print("================================================")
        print("1. Basic 'Hello World' Print Demo")
        print("2. (\\n, \\t, \\\\) Demo")
        print("3. Print traingle code challenge demo")
        print("0. Back to Main Menu")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
        
        user_choice = input("Enter your option (0-3): ").upper()
        
        if user_choice == '1':
            clear_screen()
            print("1. Basic Print Demo")
            demo_basic_print()
        elif user_choice == '2':
            clear_screen()
            print("2. Escape Characters Demo")
            demo_escape_characters()
        elif user_choice == '3':
            clear_screen()
            print("3. Print Art Demo")
            demo_print_triangle()
        elif user_choice == '0':
            type_print("\nReturning to Main Menu...")
            time.sleep(1)
            break
        else:
            type_print(f"'{user_choice}' is invalid. Please enter 0, 1, 2, or 3.")
            time.sleep(1.5)
        # each one calls on from an import from a different file, and it does so to every topic
        
        if user_choice in ('1', '2', '3'):
            input("\nPress ENTER to return to the Print Statements menu...")
    # print("================================================")
    # print("\nTOPIC 1: PRINT STATEMENTS")
    # print("\nDemonstration and trial")
    # print("EXAMPLE: \n")
    # print("print(\"Hello World\")")
    # print("Type EXIT to end trial")
    # print("================================================")

    # while True:
    #     print(print_statements.demo_basic_print())
    #     user_input = input("---> print(")
    #     if user_input.upper() == "EXIT":
    #         break







# Topic no. 2 Variables
def display_variables_submenu():
    clear_screen()
    print("================================================")
    print("TOPIC 2: VARIABLES & DATA TYPES")
    print("================================================")
    print("1. Interactive Greeting")
    print("2. String Length Calculator")
    print("3. Data Type")
    print("0. Back to Main Menu")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - -")

def topic_variables():
    while True:
        display_variables_submenu()
        user_choice = input("Enter your option (0-3): ").upper()

        if user_choice == '1':
            demo_input_greeting()
            pause_and_return()
        elif user_choice == '2':
            demo_string_length()
            pause_and_return()
        elif user_choice == '3':
            demo_data_type()
            pause_and_return()
        elif user_choice == '0':
            type_print("\nReturning to Topic Variables")
            
            break
        else:
            type_print("'{user_choice}' is invalid. Please enter a number 0-3.")
            time.sleep(1.5)



# Topic no. 3 Operattors
def display_op_submenu():
    clear_screen()
    print("================================================")
    print("TOPIC 3: OPERATORS")
    print("================================================")
    print("1. Arithmetic Operators")
    print("2. Comparison Operators")
    print("3. ATM Denomination")
    print("0. Back to Main Menu")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - -")



def op_submenu():
    while True:
        display_op_submenu()
        user_choice = input("Enter your option (0-3): ").upper()

        if user_choice == '1':
            demo_basic_arithmetic()
        elif user_choice == '2':
            demo_assignment_operators()
        elif user_choice == '3':
            demo_atm_denomination()
        elif user_choice == '0':
            type_print("\nReturning to Main Menu")
            time.sleep(1)
            break
        else:
            type_print("'{user_choice}' is invalid. Please enter a number 0-3.")
            time.sleep(1.5)
        if user_choice in ('1', '2','3'):
            input("\nPress ENTER to go back to the oonditionals menu...")

def topic_operators():
    op_submenu()

# Topic no. 4 Conditionals
def display_cond_submenu():
    clear_screen()
    print("================================================")
    print("TOPIC 4: CONDITIONAL STATEMENTS")
    print("================================================")
    print("1. Student Discount")
    print("2. Temperature Logic")
    print("3. Simple Login System")
    print("4. Even/Odd Check")
    print("5. Manga Reader Recommendation")
    print("0. Back to Main Menu")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - -")



def cond_submenu():
    while True:
        display_cond_submenu()
        user_choice = input("Enter your option (0-5): ").upper()

        if user_choice == '1':
            demo_student_discount()
        elif user_choice == '2':
            demo_temperature_logic()
        elif user_choice == '3':
            demo_simple_login()
        elif user_choice == '4':
            demo_even_odd_check()
        elif user_choice == '5':
            demo_manga_recommender()
        elif user_choice == '0':
            type_print("\nReturning to Main Menu...")
            time.sleep(1)
            break
        else:
            type_print(f"'{user_choice}' is invalid. Please enter 0-5.")
            time.sleep(1.5)

        if user_choice in ('1', '2', '3', '4', '5'):
            input("\nPress ENTER to return to the Conditionals menu...")

def topic_conditionals():
    cond_submenu()



# Topic no. 5 Loops
def for_loop_submenu():
    while True:
            clear_screen()
            print("================================================")
            print("TOPIC 5.1: FOR LOOPS")
            print("================================================")
            print("1. Count 1 to 10")
            print("2. Repeat with Time Delay")
            print("3. Countdown (Negative Step)")
            print("4. Summation with Input")
            print("5. Calculate Factorial")
            print("6. Multiplication Table Maker")
            print("7. Rocket Countdown Timer")
            print("8. Sum Odd Numbers (For + If)")
            print("0. Back to Loops Menu")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
            user_choice = input("Enter your option (0-8): ").upper()

            if user_choice == '1':
                demo_basic_for_loop()
            elif user_choice == '2':
                demo_repeat_sleep()
            elif user_choice == '3':
                demo_descending_countdown()
            elif user_choice == '4':
                demo_summation_input()
            elif user_choice == '5':
                demo_calculate_factorial()
            elif user_choice == '6':
                demo_multiplication_table()
            elif user_choice == '7':
                demo_rocket_countdown()
            elif user_choice == '8':
                demo_sum_odd_numbers()
            elif user_choice == '0':
                break
            else:
                type_print(f"'{user_choice}' is invalid. Please enter 0-8."); time.sleep(1.5)
            if user_choice in [str(i) for i in range(1, 9)]: pause_and_return() # Replaced input with pause_and_return

def while_loop_submenu():
    while True:
        clear_screen()
        print("================================================")
        print("TOPIC 5.2: WHILE LOOPS")
        print("================================================")
        print("1. Continue/Break Logic")
        print("2. Guessing Game (Break Condition)")
        print("3. Odd Number Collector (Sentinel Value)")
        print("0. Back to Loops Menu")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
        user_choice = input("Enter your option (0-3): ").upper()

        if user_choice == '1':
            demo_simple_while_break()
        elif user_choice == '2':
            demo_guessing_game()
        elif user_choice == '3':
            demo_odd_number_collector()
        elif user_choice == '0':
            break
        else:
            type_print(f"'{user_choice}' is invalid. Please enter 0-3."); time.sleep(1.5)
        if user_choice in ('1', '2', '3'): pause_and_return() # Replaced input with pause_and_return

def nested_loop_submenu():
    while True:
        clear_screen()
        print("================================================")
        print("TOPIC 5.3: NESTED LOOPS")
        print("================================================")
        print("1. Basic Iteration")
        print("2. Right-Triangle Star Pattern")
        print("3. Right-Triangle Number Pattern")
        print("4. Right-Aligned Star Triangle")
        print("5. Diamond Pattern (Advanced)")
        print("6. Composite Star Pattern (Tree)")
        print("7. Centered Number Pyramid")
        print("0. Back to Loops Menu")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
        user_choice = input("Enter your option (0-7): ").upper()

        if user_choice == '1':
            demo_basic_nested_loop()
        elif user_choice == '2':
            demo_star_triangle()
        elif user_choice == '3':
            demo_number_triangle()
        elif user_choice == '4':
            demo_right_aligned_star_triangle()
        elif user_choice == '5':
            demo_diamond_pattern()
        elif user_choice == '6':
            demo_composite_star_pattern()
        elif user_choice == '7':
            demo_number_pyramid()
        elif user_choice == '0':
            break
        else:
            type_print(f"'{user_choice}' is invalid. Please enter 0-7."); time.sleep(1.5)
        if user_choice in [str(i) for i in range(1, 9)]: input("\nPress ENTER to return...")


def loop_submenu():
    while True:
        clear_screen()
        print("================================================")
        print("TOPIC 5: LOOP")
        print("================================================")
        print("1. for loops")
        print("2. While Loops")
        print("3. Nested Lopps")
        print("0. Back to Main Menu")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
        user_choice = input("Enter your option (0-3): ").upper()

        if user_choice == '1':
            for_loop_submenu()
        elif user_choice == '2':
            while_loop_submenu()
        elif user_choice == '3':
            nested_loop_submenu()
        elif user_choice == '0':
            type_print("\nReturning to Main Menu...")
            time.sleep(1)
            break
        else:
            type_print(f"'{user_choice}' is invalid. Please enter 0-3.")
            time.sleep(1.5)

def topic_loop():
    loop_submenu()




# Topic no. 6 List
def display_lists_submenu():
    clear_screen()
    print("================================================")
    print("TOPIC 6: LISTS")
    print("================================================")
    print("1. Commnon List Operation")
    print("2. Anime List Builder")
    print("0. back to main Menu")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - -")


    
def list_submenu():
    while True:
        display_lists_submenu()
        user_choice = input("Enter your option (0-2): ").upper()


        if user_choice == '1':
            demo_list_methods()
        elif user_choice == '2':
            demo_anime_list_builder()
        elif user_choice == '0':
            type_print("\nReturning to Main Menu...")
            time.sleep(1)
            break
        else:
            type_print(f"'{user_choice}' is invalid. Please enter 0, 1, or 2.")
            time.sleep(1.5)

        if user_choice in ('1', '2'):
            input("\nPress ENTER to return to the Lists menu...")

def topic_lists():
    list_submenu()




# Topic no. 7 Functions
def display_functions_submenu():
    clear_screen()
    print("================================================")
    print("TOPIC 7: FUNCTIONS & DICTIONARIES")
    print("================================================")
    print("1. Greeter and Summation")
    print("2. Basic Dictionary Demo (Key-Value Access)")
    print("3. Anime Database (Loop + Dictionary)")
    print("4. Student Information System")
    print("0. Back to Main Menu")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")

def topic_functions():
    functions_submenu()


def functions_submenu():
    while True:
        display_functions_submenu()
        user_choice = input("Enter your option (0-4): ").upper()

        if user_choice == '1':
            demo_functions()
        elif user_choice == '2':
            demo_basic_dictionary()
        elif user_choice == '3':
            demo_interactive_dictionary()
        elif user_choice == '4':
            demo_student_info_system()
        elif user_choice == '0':
            type_print("\nReturning to Main Menu...")
            time.sleep(1)
            break
        else:
            type_print(f"'{user_choice}' is invalid. Please enter 0-4.")
            time.sleep(1.5)
        if user_choice in ('1', '2', '3'):
            input("\nPress ENTER to return to the Functions/Dictionaries menu...")





# No. 8 User-Defined Program
def user_defined_prog():
    clear_screen()
    print("="*60)
    print("OPTION 8: RUN CONTROLLED PYTHON LOGIC")
    print("="*60)
    type_print("THis progarm calls in all the imported topics or functions from all 7 topics")

    while True:
        print("================================================")
        print("Choose a Modular Operation to Run:")
        print("1. Custom Print Statement (Uses print_statements.py)")
        print("2. CHeck Variable Type (Uses variables_topic.py)")
        print("3. Perform Arithmetic (Uses operators_topic.py)")
        print("4. Test Conditional (Uses conditionals_topic.py)")
        print("5. Run Simple Loop (Uses loops_topic.py)")
        print("6. Check List for Item (Uses lists_topic.py)")
        print("7. Run Simple Function (Uses functions_topic.py)")
        print("0. Back to Main Menu")
        print("================================================")


    user_choice = input("Enter option (0-7): ")

    if user_choice == '1':
        msg = input("Enter a message: ")
        print_statements.custom_print_demo(msg)


    elif user_choice == '2':
        val = input("Enter something (number, word, True/False): ")


        if val.isdigit():
            variables_topic.get_variable_type(int(val))
        elif val.lower() == "true" or val.lower() == "false":
            variables_topic.get_variable_type(val.lower() == "true")
        else:
            variables_topic.get_variable_type(val)


    elif user_choice == '3':
        n1 = input("Enter first number: ")
        n2 = input("Enter second number: ")
        op = input("Enter operator (+, -, *, /): ")

        result = operators_topic.calculate_arithmetic(float(n1), float(n2), op)
        print("Result: ", result)


    elif user_choice == '4':
        num = int(input("Enter a whole number: "))

        result = conditionals_topic.check_even_odd(num)
        print("Result: ", result)


    elif user_choice == '5':
        numb = int(input("Enter number to count up to (1-5): "))
        loops_topic.run_simple_loop(numb)


    elif user_choice == '6':
        fruits = ['apple', 'banana', 'orange', 'grape']
        print("Current list: ", fruits)

        item = input("Enter item to search: ")
        found = lists_topic.check_item_in_list(item, fruits)
        print("Found?", found)


    elif user_choice == '7':
        name = input("Enter your name: ")
        print(functions_topic.generate_greeting(name))


    elif user_choice == '0':
        print("Rreturning to Main Menu...")
        time.sleep(1)


    else:
        print("Invalid option.")

    input("\nPress ENTER to continue...")





def main_menu():
    print("================================================")
    print("\nTopic Menu")
    time.sleep(1)
    print("Choose a topic")
    print("================================================")
    print("\n1. Print Statements")
    print("2. Variables")
    print("3. Operators")
    print("4. Conditionals (if/elif/else)")
    print("5. Loops (for/while)")
    print("6. Lists")
    print("7. Functions")
    print("8. User-Defined Program")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("9. End Program")
# This is the menu, where all the topics that had been discussed are here, andn when clicking specific number will take the user to a submenu of said topics

def main_selection():
    while True:
        clear_screen()
        main_menu()
        user_choice = input("Enter what you have chosen: ").upper()

        if user_choice == '1':
            topic_print()
        elif user_choice == '2':
            topic_variables()
        elif user_choice == '3':
            topic_operators()
        elif user_choice == '4':
            topic_conditionals()
        elif user_choice == '5':
            topic_loop()
        elif user_choice == '6':
            topic_lists()
        elif user_choice == '7':
            topic_functions()
        elif user_choice == '8':
            user_defined_prog() 
        elif user_choice == '9':
            type_print("================================================")
            type_print("\tThank you for using the menu program!!", delay=0)
            type_print("================================================")
            break
        else:
            type_print("Error: '{user_choice}' is invalid, Please enter a number from the the menu.")

main_selection()

# I had accomplished something I wouldn't have done before this, and it is to actually do it.
