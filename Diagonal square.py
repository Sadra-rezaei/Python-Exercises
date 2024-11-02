n = int(input("Enter a Number: "))
counter = 1
matrix = [[0 for i in range(n)] for j in range(n)]
i = 0
j = 0
matrix[i][j] = counter

while counter < n * n:

    # a ==> c
    if i + j >= n - 1:
        j += 1 #c
        counter += 1
        matrix[i][j] = counter

    else:
        i += 1
        counter += 1
        matrix[i][j] = counter

    #b
    while i > 0 :
        if j != n - 1:
            i -= 1
            j += 1
            counter += 1
            matrix[i][j] = counter
        else:
            break
 

    # c ==> a
    if i + j >= n - 1:
        i += 1 #a
        counter += 1
        matrix[i][j] = counter

    else:
        j += 1 #c
        counter += 1
        matrix[i][j] = counter

    if i == n -1 and j == n - 1:
        break

    #d
    while j > 0:
        if i != n - 1:
            counter += 1
            i += 1
            j -= 1
            matrix[i][j] = counter
        else:
            break



for i in range(n):
    for j in matrix[i]:
        print(j ,end=' ')
    print() 