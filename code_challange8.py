#program ask user to input a number
#ask user for a number
#loop numbers 1 to 10

print("MULTIPLICATION TABLE MAKER")

num = int(input("Enter a number: "))

print(f"\nMultiplication table for {num}:")

for i in range(1,11):
    print(f"{num} x {i} = {num * i}")