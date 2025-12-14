

# 1. Content from activity1.py (Basic Print)

def demo_basic_print():
    print("Hello World")

# 2. Content from activity3.py (Escape Characters & Formatting) 
# \n \t \r \\ demonstration
def demo_escape_characters():
    name = input("what is your name? " )
    print("WELCOME\n\t\tTO YOUR DOOM {},".format(name))
    print("\t\tyou should kys -Frisk\n \t\tcheers lads -Sans.")
    print("\rdeez\r")
    print("\"mitocondria\"")
    print("\\omning it\\")
    print("\tjamal\t")

# triangle code challenge
def demo_print_triangle():
    name = input("What is your name? ")
    print("\t\t\t\t*\n\n\n"
        "\t\t\t*\t\t*\n\n\n"
        "\t\t*\t\t\t\t*\n\n\n"
        "\t*\t\t\t\t\t\t*\n\n\n"
        "*\t\t\tHi\t\033[34m{}\033[0m\t\t\t\t*\n\n\n"
        "\t*\t\t\t\t\t\t*\n\n\n"
        "\t\t*\t\t\t\t*\n\n\n"
        "\t\t\t*\t\t*\n\n\n"
        "\t\t\t\t*".format(name))

# OPTIONAL: Run all demos for the main menu Topic 1 selection
def run_topic_1_all():
    """Runs all print demonstrations sequentially for the main menu selection."""
    print("\n" + "="*50)
    print("TOPIC 1: PRINT STATEMENTS DEMONSTRATION")
    print("="*50)
    
    print("\n1. Basic Hello World (activity1.py)")
    demo_basic_print()
    
    print("\n2. Escape Character & Formatting (activity3.py)")
    demo_escape_characters()
    
    print("\n3. Complex Print Art & Color (code_challange.py)")
    demo_print_triangle()()
    print("\n" + "="*50)


def custom_print_demo(message):
    print("---------------------------------")
    print(f"Modular Print Output: {message.upper()}")
    print("---------------------------------")