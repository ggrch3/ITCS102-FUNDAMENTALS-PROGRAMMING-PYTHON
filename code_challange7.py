print("ODD NUMBER SUMMATION")
num = eval(input("Enter a number: "))

sum = 0

for i in range(10):
    if num % 2 == 1:
        sum += num  

print("The sum of odd number is", sum)