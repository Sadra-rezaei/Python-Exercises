n , m = input().split()
flag = 2
n = [int(n) for n in input().split()]
m = [int(m) for m in input().split()]
for i in n:
    if i == 0:
        if flag == 1:
            print("YES")
            exit()
        else:
            flag = 0
    elif i == 1:
        if flag == 0:
            print("YES")
            exit()
        else:
            flag = 1
print("NO")