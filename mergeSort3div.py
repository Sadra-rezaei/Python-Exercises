import random

# ====================== regular mergesort ========================


def merge(left, right, lsize, rsize):
    res = []
    leftindex = 0
    rightindex = 0

    while rightindex != rsize and leftindex != lsize:


        if right[rightindex] < left[leftindex]:

            res.append(right[rightindex])
            rightindex += 1
            if rightindex == rsize:
                res.extend(left[leftindex: lsize])
                break


        else:

            res.append(left[leftindex])
            leftindex += 1
            if leftindex == lsize:
                res.extend(right[rightindex: rsize])
                break

    return res



def mergesort(list, n):
    k = int(n /2)
    left = []
    right = []

    if n == 1:
        return list
    
    if n == 2:
        if list[0] > list[1]:
            list[0] += list[1]
            list[1] = list[0] - list[1]
            list[0] -= list[1]
        return list
    

    for i in range(n):
        if i < k:
            left.append(list[i])
        else:
            right.append(list[i])


    left = mergesort(left, len(left))
    right = mergesort(right, len(right))
    return merge(left, right, k, n - k)




n = int(input("list lengh: "))
list = []

for i in range(n):
    list.append(random.randint(0, n * 2))

print(list, "\n")

list = mergesort(list, n)

print(list)
