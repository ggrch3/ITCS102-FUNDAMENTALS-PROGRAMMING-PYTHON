



import random,time

print("Let's go GAMBLING :D")
time.sleep(1)
r = input("Are you ready :) --> ")

random_number = random.randint(1, 100)
tries = 0
con = True

while True:
    num = int(eval(input("Input your number - - - > ")))

    con += 1 

    if num == random_number: 
        print("You are Right!")
        print(f"Crazy that it only took {con} tries")
        break
    else:
        print("Wrong mate!")
        print("play again...")
        continue