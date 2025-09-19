

odd_sum = 0
for i in range(1,11,1):
    num = eval(input(f"{i} - Enter a number --> "))
    
    if num % 2 == 1:
        odd_sum += num

print(f"The Sum of All ODD numbers is --> {odd_sum}")
