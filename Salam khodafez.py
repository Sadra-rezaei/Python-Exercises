x = int(input())
myInputList = [n for n in input().split()]

classroom = []
for person in myInputList:
    if person == myInputList[0]:
        classroom.append(person)
    else:
        for i in range(0, len(classroom)):
            print(person + ": salam", classroom[-1 * (i + 1)] + '!')
        classroom.append(person)


for i in range(0, len(classroom)):
    print(classroom[0] + ": khodafez bacheha!")
    if classroom[0] != classroom[-1]:
        for j in range(1, len(classroom)):
            print(classroom[j] + ": khodafez", classroom[0] + '!')
        classroom.remove(classroom[0])