x = int(input("Enter a number: "))
n = 0
while int(x / (10 ** n)) != 0:
    n = n + 1
z = 1
while z != n + 1:
    if int(x /(10 ** (n - z)))%10 == int(x /(10 ** (z - 1)))%10 :
        z = z + 1
    else:
        print("False")
        exit()
print("True")