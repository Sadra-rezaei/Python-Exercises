x = input("Enter a number: ")
y = x.isdigit() #aya digit hast?
if y == False:
    print("error")
    exit()
else:
    x = int(x)
if 0 <= x <= 100:
    print("no charge")
elif 100 < x <= 200:
    print((x - 100) * 5)
elif 200 < x:
    print(((x - 200) * 10) + 500)