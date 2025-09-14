#ascending order
#descending order 20 - 1

import time 

print("Countdown in T minus 20 seconds")
time.sleep(1)

for x in range(20, 0, -1):
    time.sleep(1)
    print(x)