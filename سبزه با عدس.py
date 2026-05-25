n, k = input().split()
n = int(n)
k = int(k)

list = [None]*n
step = 2
start = 0

while (k != 0):
    for i in range(start, n, step):
        list[i] = "*"
        k -= 1
        if k == 0:
            break

    if k == 1 and list[n - 1] == None:
        k -= 1
        list[n - 1] = "*"

    step *= 2
    start = start * 2 + 1

pairCounter = 0

for i in range(n - 1):
    if (list[i] == "*" and list[i + 1] == "*"):
        pairCounter += 1

print(pairCounter)
