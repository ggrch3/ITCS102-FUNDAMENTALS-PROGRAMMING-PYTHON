
Clean = True 

while Clean == True:
    qst = input("Are the clothes clean ? (yes/no): ")

    if qst.lower() == "yes":
        print("Loop Continue")
        continue 

     
    else:
        print("Loop Stops")
        break