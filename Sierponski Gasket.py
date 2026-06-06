

n = int(input("Enter: "))
prev= [1]
for i in range(n):
    out = ['*' if x%2 == 1 else ' ' for x in prev]
    print(' '*((n-i)//2), *out, sep='')
    prev = [1] + [prev[x] + prev[x-1] for x in range(1,len(prev))] + [1]