myList = [int(n) for n in input().split()]
myList.sort()

if myList[0] == myList[-1]:
    print("All numbers are equal")
elif myList[0] != myList[1] and myList[1] == myList[2] and myList[2] == myList[3] and myList[3] == myList[4]:
    print("Four numbers are equal")
elif myList[0] == myList[1] and myList[1] == myList[2] and myList[2] == myList[3] and myList[3] != myList[4]:
    print("Four numbers are equal")

elif myList[0] == myList[1] and myList[1] == myList[2] and myList[2] != myList[3] and myList[3] == myList[4]:
    print("three numbers and two numbers are equal")
elif myList[0] == myList[1] and myList[1] != myList[2] and myList[2] == myList[3] and myList[3] == myList[4]:
    print("thee numbers and two numbers are equal")

elif myList[0] == myList[1] and myList[1] != myList[2] and myList[2] == myList[3] and myList[3] != myList[4]:
    print("numbers are equal two by two")
elif myList[0] == myList[1] and myList[1] != myList[2] and myList[2] != myList[3] and myList[3] == myList[4]:
    print("numbers are equal two by two")
elif myList[0] != myList[1] and myList[1] == myList[2] and myList[2] != myList[3] and myList[3] == myList[4]:
    print("numbers are equal two by two")

elif myList[0] == myList[2] or myList[1] == myList[3] or myList[2] == myList[4]:
    print("three numbers are equal")

elif myList[0] == myList[1] or myList[1] == myList[2] or myList[2] == myList[3] or myList[3] == myList[4]:
    print("two numbers are equal")

else:
    print("none of them are equal")