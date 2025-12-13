
import time
import random


# FOR LOOP 


# 1. Content from activity16.py (Basic For Loop)
def demo_basic_for_loop():
    print("For Loop Demo 1: Count 1 to 10")
    for i in range(1, 11, 1):
        print(i, end=" ")
    print("\n" + "=" * 40)

# 2. Content from activity12.py (Simple For Loop with Delay)
def demo_repeat_sleep():
    print("For Loop Demo 2: Repeat with Time Delay")
    for i in range(3):
        time.sleep(1)
        print(f"Repeat ({i+1})")
    print("=" * 40)

# 3. Content from activity14.py (Countdown/Negative Step)
def demo_descending_countdown():
    print("For Loop Demo 3: Countdown (Negative Step)")
    print("Countdown in T minus 5 seconds")
    time.sleep(1)
    
    for x in range(5, 0, -1):
        time.sleep(1)
        print(x)
    print("BLAST OFF!")
    print("=" * 40)

# 4. Content from activity13.py (For Loop with Summation)
def demo_summation_input():
    print("For Loop Demo 4: Summation with Input (5 numbers)")
    num_sum = 0
    print("Enter 5 numbers to get the total sum.")
    for x in range(1, 6):
        try:
            number = eval(input(f"Insert number {x}: "))
            num_sum += number
        except NameError:
            print("Invalid input, skipping number.")
    print("Total Sum:", num_sum)
    print("=" * 40)
    
# 5. Content from code_challange6.py (Factorial Calculation)
def demo_calculate_factorial():
    print("For Loop Demo 5: Factorial Program")
    try:
        num = int(input("Enter a number for factorial: "))
    except ValueError:
        print("Invalid input. Factorial skipped.")
        return
        
    result = 1
    print(f"Calculating factorial of {num}:")
    for x in range(num, 0, -1):
        result *= x
        print(f"x={x}, result={result}")
    
    print(f"The Factorial of {num} is {result}")
    print("=" * 40)

# 6. Content from code_challange8.py (Multiplication Table)
def demo_multiplication_table():
    print("For Loop Demo 6: Multiplication Table Maker")
    try:
        num = int(input("Enter a number to multiply (1-10): "))
    except ValueError:
        print("Invalid input. Table skipped.")
        return
        
    print(f"\nMultiplication table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print("=" * 40)

# 7. Content from code_challange9.py (Rocket Countdown)
def demo_rocket_countdown():
    print("For Loop Demo 7: Rocket Countdown Timer")
    try:
        start = int(input("Enter the time for countdown: "))
    except ValueError:
        print("Invalid input. Countdown skipped.")
        return
        
    print("\nCountdown started in T minus ")
    for i in range(start, 0, -1):
        time.sleep(0.5)
        print(i)
    print("LIFT OFF!")
    print("=" * 40)


# II. WHILE LOOP 


# 8. Content from activity21.py (Basic While Loop/Continue/Break)
def demo_simple_while_break():
    print("While Loop Demo 1: Continue/Break Logic")
    while True:
        confirm = input("Continue(y/n)-->").lower() 
        if confirm == 'y': 
            print("Continuing loop...")
            continue
        elif confirm == 'n':
            print("STOPPING loop.")
            break
        else:
            print("Invalid input. Please type 'y' or 'n'.")
            continue
    print("Loop finished.")
    print("=" * 40)
    
# 9. Content from activity22.py (Advanced While Loop / Guessing Game)
def demo_guessing_game():
    print("While Loop Demo 2: Guessing Game (Break Condition)")
    random_number = random.randint(1, 10)
    tries = 0
    print("Guess a number between 1 and 10.")
    
    while True:
        tries += 1
        try:
            num = int(input(f"Attempt {tries}: Enter your number: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if num == random_number: 
            print("You are Right! The number was", random_number)
            print(f"Crazy that it only took {tries} tries")
            break
        else:
            print("Wrong mate!")
            if num > random_number:
                print("Too high!")
            else:
                print("Too low!")
            continue
    print("Game Over.")
    print("=" * 40)

# 10. Content from code_challange14.py (Odd Number Collector)
def demo_odd_number_collector():
    print("While Loop Demo 3: Odd Number Collector (Sentinel Value)")
    total_sum = 0
    odd_list = []
    isODD = True
    print("Type '0' to terminate the loop and see the results.")
    
    while isODD == True:
        try:
            num = int(input("Enter number --> "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
            
        if num == 0:
            print("Loop Terminated by '0'.")
            isODD = False 
        elif num % 2 == 1: 
            print("ODD number detected.")
            odd_list.append(str(num))
            total_sum += num
        elif num % 2 == 0:
            print("EVEN number detected, not counted.")
            
    print(f"The sum of all the ODD numbers is: {total_sum}")
    print(f"All ODD numbers collected: {', '.join(odd_list)}")
    print("=" * 40)
    
# 11. Content from activity15.py and code_challange7.py (For Loop with Conditional Sum)
def demo_sum_odd_numbers():
    print("Loop/Conditional Demo 4: Summing Odd Numbers (10 inputs)")
    odd_sum = 0
    for i in range(1, 11):
        try:
            num = int(input(f"{i} - Enter a number --> ")) 
            if num % 2 == 1:
                odd_sum += num
        except ValueError:
            print("Invalid input, skipping.")

    print(f"The Sum of All ODD numbers entered is --> {odd_sum}")
    print("=" * 40)


# NESTED LOOP 


# 12. Content from activity17.py (Basic Nested Loop)
def demo_basic_nested_loop():
    print("Nested Loop Demo 1: Basic Iteration")
    for x in range(1, 4):
        print(f"Outer Loop Iteration {x}: ", end="")
        for i in range(1, 4):
            print(i, end=" ")
        print()
    print("=" * 40)

# 13. Content from activity19.py (Right-Triangle Star Pattern)
def demo_star_triangle():
    print("Nested Loop Demo 2: Right-Triangle Star Pattern")
    for i in range (1, 6):
        for y in range(1, i):
            print('*', end=' ')
        print()
    print("=" * 40)

# 14. Content from activity18.py (Right-Triangle Number Pattern)
def demo_number_triangle():
    print("Nested Loop Demo 3: Right-Triangle Number Pattern")
    for i in range (1, 6):
        for y in range(1, i):
            print(y, end=' ')
        print()
    print("=" * 40)

# 15. Content from code_challange10.py (Right-Aligned Star Triangle)
def demo_right_aligned_star_triangle():
    print("Nested Loop Demo 4: Right-Aligned Star Triangle")
    rows = 5
    for i in range(1, rows + 1):
        for y in range(rows, i, -1):
            print("  ", end="")
        for z in range(1, i + 1):
            print("* ", end="")
        print()
    print("=" * 40)

# 16. Content from code_challange11.py (Diamond Pattern)
def demo_diamond_pattern():
    print("Nested Loop Demo 5: Diamond Pattern (Advanced)")
    size = 5
    for i in range(1, size + 1):
        print(" " * (size - i), end="")
        print("* " * i)
    for i in range(size - 1, 0, -1):
        print(" " * (size - i), end="")
        print("* " * i)
    print("=" * 40)

# 17. Content from code_challange13.py (Composite Star Pattern - Tree)
def demo_composite_star_pattern():
    print("Nested Loop Demo 6: Composite Star Pattern (Tree)")
    size = 5
    for part in range(3):
        for i in range(1, size + 1):
            print(" " * (size - i), end="")
            print("* " * i)
    for _ in range(2):
        print(" " * (size - 1) + "***")
    print("=" * 40)

# 18. Content from code_challange12.py (Number Pyramid Pattern)
def demo_number_pyramid():
    print("Nested Loop Demo 7: Centered Number Pyramid")
    rows = 7
    for w in range(1, rows + 1):
        print("  " * (rows - w), end="")
        for y in range(w, 0, -1):
            print(y, end=" ")
        for z in range(2, w + 1):
            print(z, end=" ")
        print()
    print("=" * 40)

# MASTER FUNCTION: Run all demos for the main menu Topic 5 selection
def run_topic_5_all():
    print("\n" + "="*50)
    print("TOPIC 5: LOOP STATEMENTS (FOR/WHILE/NESTED) DEMONSTRATION")
    print("="*50)
    
    # FOR LOOPS
    demo_basic_for_loop()
    demo_repeat_sleep()
    demo_descending_countdown()
    demo_summation_input()
    demo_calculate_factorial()
    demo_multiplication_table()
    demo_rocket_countdown()
    demo_sum_odd_numbers()
    
    # WHILE LOOPS
    demo_simple_while_break()
    demo_guessing_game()
    demo_odd_number_collector()
    
    # NESTED LOOPS
    demo_basic_nested_loop()
    demo_star_triangle()
    demo_number_triangle()
    demo_right_aligned_star_triangle()
    demo_diamond_pattern()
    demo_composite_star_pattern()
    demo_number_pyramid()

    print("\n" + "="*50)
    print("All Loop types demonstrated.")
    print("="*50)


def run_simple_loop(end_num):
    print(f"Running 'for i in range(1, {end_num} + 1)':")
    for i in range(1, end_num + 1):
        print(f"Loop Count: {i}")