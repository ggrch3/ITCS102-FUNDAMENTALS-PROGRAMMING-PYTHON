print("Factorial Program")

num = eval(input("Enter a number - - > "))
result = 1
 
for x in range(num, 0, -1):
	print(x,"- - - -", result)
	result *= x

print("The Factorial of", num, "is", result)