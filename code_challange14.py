import time


name = input("Hi, what is your name --> ")
time.sleep(2)
print("+++++++++++++++++++++++++++++++++++++++++++")

time.sleep(3)
print("ODD number compiler, type '0' to terminate the loop")

total_sum = 0
odd = ""
isODD = True

while isODD == True:
    num = eval(input("Enter number --> "))
    if num % 2 == 1: 
        print("ODD number detected")
        odd += str(num) + ","
        total_sum += num
        continue
    elif num == 0:
        print("Loop Terminated")
        break
    else:
        if num % 2 == 0:
            print("EVEN number detected, moving on kahit di maka move-on :/")
        else:
            print("invalid")
        continue

print(f"{name}, The sum of all the ODD is {total_sum}")
print(f"all of the ODD is {odd}")


#past lessons for reference

# odd_sum = 0

# for i in range(1,11,1):
#     num = eval(input(f"{i} - Enter a number --> "))
    
#     if num % 2 == 1:
#         odd_sum += num

# print(f"The Sum of All ODD numbers is --> {odd_sum}")

