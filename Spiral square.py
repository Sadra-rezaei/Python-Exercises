n = int(input("Enter a Number: "))
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)


counter = 1
x = n
y = 0
while counter <= n*n:
    # a:
    i = x - 1
    for j in range(y, x):
        matrix[i][j] = counter
        counter += 1

    # b:
    j = x - 1
    for i in range(x - 2, y-1, -1):
        matrix[i][j] = counter
        counter += 1



    # c:
    i = y
    for j in range(x - 2, y-1, -1):
        matrix[i][j] = counter
        counter += 1


    # d:
    j = y
    for i in range(y+1, x - 1):
        matrix[i][j] = counter
        counter += 1


    x -= 1
    y += 1

for t in range(n):
    for p in range(n):
        print(matrix[t][p], end=" ")
    print()
