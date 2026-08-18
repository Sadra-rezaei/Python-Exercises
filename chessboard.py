
def printchess(n, chess):
    for i in range(n):
        for j in range(n):
            print(chess[i][j], end=" ")
        print()


n = 16    #lenth of the board
l = 2     #lenth of the houses

chess = [['0' for _ in range(n)]for _ in range(n)]



for x in range(0,n,l):
    for y in range(0,n,l):

        if (x + y) % (l*2) == l:   # Try " == l "

            for i in range(l):
                for j in range(l):
                        
                        chess[x + i][y + j] = '.'


printchess(n, chess)