#words and something in between

name = input("Insert your name --> ")
IsStudent = input("Are you a student (Yes/No) --> ")
fare = eval(input("payment -> "))

import time

print("\nVerifying if student status...")
time.sleep(2)


if IsStudent.lower() == "yes" :
	discount = fare * .2
	new_fare = fare - discount
	print("Hi", name," Verification finished✓")
	time.sleep(1)
	print("Discount fare is:", new_fare)
else:
	print("There seems to have a problem.")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print("It seems that you are not a student", name," no discount applied,")
	time.sleep(1)
	print("womp")
	time.sleep(1)
	print("womp")
	time.sleep(1)
	print("Fare is -", fare)