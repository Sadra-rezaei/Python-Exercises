class House:
    def __init__(self):
        self.isGroup = False
        self.isHouse = True

    def changeHouse(self):
        self.isHouse = not self.isHouse

def printMatrix(M ,row, col):
    print()
    for i in range(row):
        for j in range(col):
            if M[i][j].isHouse or M[i][j].isGroup:
                print('O',end=" ")

                # print("i = ", i, ", j = ", j)

            else:
                print('X',end=" ")
        print()

def reversLine(M, row, col):
    for j in range(col):
        M[row][j].changeHouse()

m, n, k = map(int, input().split())

table = [[House() for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
            table[i][j].isHouse = False

printMatrix(table,m,n)
reversLine(table,1,n)
printMatrix(table,m,n)