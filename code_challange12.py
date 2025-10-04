



for w in range(1, 8):
    for x in range(8, w, -1):
        print(" ", end=" ")
    for y in range(w, 0, -1):
        print(y, end=" ")
    for z in range(1, w):
        print(w, end=" ")

    
    print()
