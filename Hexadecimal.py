
num16 = input()
myList = []
for i in num16:
    myList.append(i)

if myList[-1] == 'F':
    for i in range(0,len(myList)):
        if myList[-1*(i+1)] == "F":
            if -1*(i+1) != -1*len(myList):
                myList[-1*(i+1)] = "0"
            else:
                myList[-1*(i+1)] = "10"
        else:
            if myList[-1*(i+1)] == "9":
                myList[-1*(i+1)] = "A"
            elif myList[-1*(i+1)] == "A":
                myList[-1 * (i + 1)] = "B"
            elif myList[-1*(i+1)] == "B":
                myList[-1 * (i + 1)] = "C"
            elif myList[-1*(i+1)] == "C":
                myList[-1 * (i + 1)] = "D"
            elif myList[-1*(i+1)] == "D":
                myList[-1 * (i + 1)] = "E"
            elif myList[-1*(i+1)] == "E":
                myList[-1 * (i + 1)] = "F"
            else:
                myList[-1 * (i + 1)] = str(int(myList[-1*(i+1)])+1)
            break
else:
    if myList[-1] == "9":
        myList[-1] = "A"
    elif myList[-1] == "A":
        myList[-1] = "B"
    elif myList[-1] == "B":
        myList[-1] = "C"
    elif myList[-1] == "C":
        myList[-1] = "D"
    elif myList[-1] == "D":
        myList[-1] = "E"
    elif myList[-1] == "E":
        myList[-1] = "F"
    else:
        myList[-1] = str(int(myList[-1]) + 1)

new_string = ""
for i in myList:
    new_string += i

print(new_string)
print("Hello World")
