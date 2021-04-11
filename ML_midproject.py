import math
import random
for i in range(20):
    velocity = random.randint(0,100)
    angle = math.radians(random.randint(0,91))
    xi = velocity*math.cos(angle)
    yi = velocity*math.sin(angle)
    H = (velocity**2)*(math.sin(angle)**2)/(2*9.8)
    R = (velocity**2)*(math.sin(angle*2))/9.8
    print(round(H,3), round(R,3))