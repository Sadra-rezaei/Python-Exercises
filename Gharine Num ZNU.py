def counterOfDigits(number):
    m = number
    result = 1
    while m >= 10:
        m = m / 10
        result += 1
    return result

number = int(input("Enter a number: "))
i = counterOfDigits(number)
j = 0
sum = 0
while i != 0:
    sum += (int(number / (10 ** j)) % 10) * (10 ** (i - 1))
    j += 1
    i -= 1
print(sum * 5)