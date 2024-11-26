number1 , number2 = input().split()
number1 = int(number1)
number2 = int(number2)

temp = number1 - number2
if temp < 0:
    temp = - temp

for i in range(2 , temp + 1):
    if temp % i == 0:
        print(i, end=" ")