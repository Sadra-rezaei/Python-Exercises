def removeAll(list):
    for k in list:
        if k == '0':
            list.remove(k)
    return list

turn = int(input())
result = []

for h in range(turn):
    firstInput = input()
    secondInput = input()
    firstTemp = list(firstInput)
    secondTemp = list(secondInput)
    flag = False
    firstReversTemp = list(reversed(firstTemp))

    for i in range(len(secondTemp)):
        for j in range(len(firstTemp)):
            if secondTemp[i] == firstTemp[j]:
                if i == len(secondTemp) - 1:
                    flag = True
                    break
                else:
                    firstTemp[j] = '0'
                    removeAll(firstTemp)
                    break
            else:
                if j == len(firstTemp) - 1:
                    break
                else:
                    firstTemp[j] = '0'

    if flag != True:
        for i in range(len(secondTemp)):
            for j in range(len(firstReversTemp)):
                if secondTemp[i] == firstReversTemp[j]:
                    if i == len(secondTemp) - 1:
                        flag = True
                        break
                    else:
                        firstReversTemp[j] = '0'
                        removeAll(firstReversTemp)
                        break
                else:
                    if j == len(firstReversTemp) - 1:
                        break
                    else:
                        firstReversTemp[j] = '0'

    if flag == True:
        result.append("YES")
    else:
        result.append("NO")

for ans in result:
    print(ans)