import math
a = float(input())
b = float(input())
c = float(input())

delta = (b * b) - (4 * a * c)

if a != 0 or b != 0:
    if delta < 0:
        print("IMPOSSIBLE")

    elif delta == 0:
        print('%.3f' %((-1 * b) / (2 * a)))

    else:
        delta = math.sqrt(delta)
        print('%.3f' %((-1 * b - delta) / (2 * a)))
        print('%.3f' %((-1 * b + delta) / (2 * a)))

elif a == 0 and b != 0:
    print('%.3f' %((-1 * c) / b))

else:
    print("IMPOSSIBLE")