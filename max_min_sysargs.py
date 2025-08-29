import sys
import math
max=-math.inf
min=+math.inf
for i in range(0,len(sys.argv)):
    if int(sys.argv[i])>max:
        max=int(sys.argv[i])
for i in range(0,len(sys.argv)):
    if int(sys.argv[i])>min:
        min=int(sys.argv[i])
print("maximum:",max)
print("minimum",min)
