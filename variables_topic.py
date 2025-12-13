

# 1. Content from activity2.py (Basic Input and String Variable)
def demo_input_greeting():
    """Demonstrates basic input, variable assignment, and string formatting."""
    print("--- Variable Demo 1: Input and Greeting ---")
    name = input("What is your name? ")
    
    # Python convention: print() statements should be used for output
    print("Hi {} Welcome to the system!".format(name))
    print("-" * 40)

# 2. Content from activity4.py (String Variables and the len() Function)
def demo_string_length():
    print("--- Variable Demo 2: String Length (len() function) ---")
    name = input("Your name here --> ")
    
    # len() returns the length of the string variable
    print("Your name has", len(name), "Characters")
    print("-" * 40)

# 3. Content from activity5.py (Data Types and eval())
def demo_data_type():
    print("Variable Demo 3: Checking Data Type (eval() and type())")
    
    z = eval(input("Enter a value (e.g., 'hello', 123, 1.23) --> "))
    
    print("The variable 'z' contains data of type:", type(z))
    print("-" * 40)

# MASTER FUNCTION: Run all demos for the main menu Topic 2 selection
def run_topic_2_all():
    print("\n" + "="*50)
    print("TOPIC 2: VARIABLES & INPUT DEMONSTRATION")
    print("="*50)
    
    # Call all demo functions
    demo_input_greeting()
    demo_string_length()
    demo_data_type()
    
    print("\n" + "="*50)
    print("Variables, data types, and user input demonstrated.")
    print("="*50)


def get_variable_type(value):
    type_name = type(value).__name__
    print(f"Value: '{value}' has a Data Type of: \033[92m{type_name}\033[0m")