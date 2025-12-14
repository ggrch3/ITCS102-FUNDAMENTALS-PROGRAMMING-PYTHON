

# 1. Content from activity6.py (Basic Arithmetic Operator)
def demo_basic_arithmetic():
    print("Operator Demo 1: Basic Arithmetic")
    x = eval(input("Input number here -> "))
    print(f"69 * {x}")
    y = 69 * x
    print("The answer is", y)
    print("=" * 40)

# 2. Content from activity7.py (Assignment Operators)
# +=, -=, *=, /=."""
def demo_assignment_operators():
    
    print("Operator Demo 2: Assignment Operators")
    x = 5
    print("Initial value of x is", x) 
    
    x += 10
    print("After x += 10, x is", x)
    
    x -= 3
    print("After x -= 3, x is", x)
    
    x *= 30
    print("After x *= 30, x is", x)
    
    x /= 2
    print("After x /= 2, x is", x)
    print("=" * 40)

# 3. Content from activity8.py (Comparison Operators)
def demo_comparison_operators():
    print("Operator Demo 3: Comparison Operators (Returns Boolean)")
    b = 3
    a = 3
    name1 = 'Geroche'
    name2 = 'Paul'
    
    print(f"Is b (3) equal to a (3)? -> {b == a}")
    print(f"Is name1 ('Geroche') NOT equal to name2 ('Paul')? -> {name1 != name2}")
    
    balance = 500
    withdrawal = 1500
    print(f"Is balance ({balance}) greater than or equal to withdrawal ({withdrawal})? -> {balance >= withdrawal}")
    print("=" * 40)

# 4. Content from activity9.py (Logical/Complex Comparison)
def demo_logical_operators():
    print("Operator Demo 4: Logical Operators (Boolean Logic)")
    x = 'George'
    y = 'qwerty'
    
    # Example: (x is not 'George') LESS THAN OR EQUAL TO (y is not 'qwerty')
    print(f"(x != 'George') <= (y != 'qwerty') evaluates to: {(x != 'George') <= (y != 'qwerty')}") 
    print("=" * 40)

# 5. Content from code_challange2.py (Floor Division and Modulus)
def demo_atm_denomination():
    print("Operator Demo 5: Advanced Arithmetic (ATM Denominations)")
    try:
        x = eval(input("Enter the total amount to withdraw: "))
    except NameError:
        print("Invalid input. Please enter a number.")
        return
        
    print(f"Calculating denominations for {x}...")

    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    amount = x
    
    for note in denominations:
        count = amount // note
        amount = amount % note
        print(f"| {count} x {note} |")

    print("Remaining amount:", amount)
    print("=" * 40)

# MASTER FUNCTION: Run all demos for the main menu Topic 3 selection
def run_topic_3_all():
    print("\n" + "="*50)
    print("TOPIC 3: OPERATORS DEMONSTRATION")
    print("="*50)
    
    demo_basic_arithmetic()
    demo_assignment_operators()
    demo_comparison_operators()
    demo_logical_operators()
    demo_atm_denomination()
    
    print("\n" + "="*50)
    print("All Operator types demonstrated.")
    print("="*50)

def calculate_arithmetic(num1, num2, op):
    """Performs a single arithmetic calculation."""
    if op == '+': 
        return num1 + num2
    elif op == '-': 
        return num1 - num2
    elif op == '*': 
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:

        return "Error: Invalid operator."
