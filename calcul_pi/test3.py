import math
import time
def Un(n):
    return str(round(n*math.sin(360*math.pi/180/(2*n)),10))

for i in range(3,10000):
    print(f"U({i}) = {Un(i)}     ",end='\r')
    time.sleep(0.01)
print(f"U({i}) = {Un(i)}     ")