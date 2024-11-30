num = int(input("Enter a number: "))
starList = []
starString = ""

for i in range(num):
    starList.append("*")
    starString = "".join(starList)
    print(starString)
