#Rocket Countdown Timer Simulator
#Program ask for starting numer
import time

start = int(input("Enter the time for countdown: "))

print("\ncountdown started in T minus ")
for i in range(start, 0, -1):
    time.sleep(1)
    print(i)
print("LIFT OFF!")