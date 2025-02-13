from sys import flags

t = int(input())
flag = []
if t < 0 or t > 10000:
    print("Invalid Turn")
    exit()
for flag_V in range(t):
    flag.append(False)
for count in range(0 ,t):
    n = [int(n) for n in input().split()] #n = tedad
    r = [int(r) for r in input().split()] #r = rotbe ostani
    p = [int(p) for p in input().split()] #p = soalat javab dade shode
    R = int(input()) #R = rotbe keshvari
    if R < 1 or R > 1603:
        print("Error")
        break
    if R <= 40:
        flag[count] = True
    else:
        for i in range(0, 6):
            if 1 <= r[i] <= n[i] <= 1000 and 0 <= p[i] <= 6:
                pass
            else:
                print("Error")
                break
            if n[i] >= 7 and r[i] == 1 and p[i] >= 2:
                flag[count] = True
for javab in range(t):
    if flag[javab] == True:
        print("YES")
    else:
        print("NO")