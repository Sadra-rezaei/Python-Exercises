def Fact(n):
    count, F = 0, 1
    while count < n:
        count += 1
        F *= count #F = Factorial
    return F




r = float(input("Enter a angle: "))
r = (r * 3.1415) / 180
k = 1.0
i = 1.0
res = 0.0

while i <= 19:
    res += k * ((r ** i) / Fact(i))
    k *= -1
    i += 2

print('%.10f' % res)