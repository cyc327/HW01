import math
import random
for i in range(20):
    velocity = random.uniform(0,100)
    angle = math.radians(random.uniform(1,91))
    xi = velocity*math.cos(angle)
    yi = velocity*math.sin(angle)
    H = (velocity**2)*(math.sin(angle)**2)/(2*9.8)
    R = (velocity**2)*(math.sin(angle*2))/9.8
    print("v =","{:8.4f}".format(velocity), "a =", "{:8.4f}".format(angle))    
    print("H =","{:8.3f}".format(H), "R =","{:8.3f}".format(R))
    print("\t")