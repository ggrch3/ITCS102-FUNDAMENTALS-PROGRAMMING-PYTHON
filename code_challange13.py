




for a in range(1, 4):
    for b in range(10, a, -1):
        print(" ", end=" ")
    for c in range(1, 2*a):
        print("*", end=" ")
    print()
for a in range(2, 0, -1):
    for b in range(10, a, -1):
        print(" ", end=" ")
    for c in range(1, 2*a):
        print("*", end=" ")
    print()
for w in range(4):  
    for x in range(1, 11):
        for y in range(10, x, -1):
            print(" ", end=" ")
        for z in range(1, 2*x, 1):
            print("*", end=" ")
        print()
for i in range(4):  
    for j in range(8):  
        print(" ", end=" ")
    for j in range(3):  
        print("*", end=" ")
    print()