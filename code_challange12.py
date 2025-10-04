



for i in range(1, 8):
    for x in range(8, i, -1):
        print(" ", end=" ")
    for y in range(i, 0, -1):
        print(y, end=" ")
    for z in range(1, i):
        print(i, end=" ")
    print()