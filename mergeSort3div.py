import random

# ====================== 3 div mergesort ========================

def merge2(left, right, lsize, rsize):
    res = []
    leftindex = 0
    rightindex = 0

    while leftindex < lsize and rightindex < rsize:
        if right[rightindex] < left[leftindex]:
            res.append(right[rightindex])
            rightindex += 1
        else:
            res.append(left[leftindex])
            leftindex += 1

    res.extend(left[leftindex:])
    res.extend(right[rightindex:])
    return res


def merge(left, mid, right, lsize, msize, rsize):
    res = []
    leftindex = 0
    midindex = 0
    rightindex = 0

    # print(left, mid, right)
    # print(lsize, msize, rsize)

    while rightindex != rsize and leftindex != lsize and midindex != msize:

        # print(leftindex, midindex, rightindex)

        if right[rightindex] <= left[leftindex] and right[rightindex] <= mid[midindex]:

            res.append(right[rightindex])
            rightindex += 1
            if rightindex == rsize:
                res.extend(merge2(left[leftindex:], mid[midindex:], lsize - leftindex, msize - midindex))
                break
        
        elif mid[midindex] <= right[rightindex] and mid[midindex] <= left[leftindex]:

            res.append(mid[midindex])
            # print(mid[midindex], res) #================
            midindex += 1
            if midindex == msize:
                res.extend(merge2(left[leftindex:], right[rightindex:], lsize - leftindex, rsize - rightindex))
                break

        elif left[leftindex] <= right[rightindex] and left[leftindex] <= mid[midindex]:

            res.append(left[leftindex])
            leftindex += 1
            if leftindex == lsize:
                res.extend(merge2(right[rightindex:], mid[midindex:], rsize - rightindex, msize - midindex))
                break

    return res



def mergesort(arr, n):
    k = int(n /3)
    w = n - k
    left = []
    mid = []
    right = []

    
    if n <= 1:
        return arr
    
    if n == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    

    for i in range(n):
        if i < k:
            left.append(arr[i])
        elif i >= k and i < w:
            mid.append(arr[i])
        else:
            right.append(arr[i])


    left = mergesort(left, len(left))
    mid = mergesort(mid, len(mid))
    right = mergesort(right, len(right))
    return merge(left, mid, right, k, w - k, n - w)




n = int(input("list lengh: "))
arr = []

for i in range(n):
    arr.append(random.randint(0, n * 2))

print(arr, "\n")

arr = mergesort(arr, n)

print(arr)