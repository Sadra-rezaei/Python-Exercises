first_number = int(input()) #dota adad gereftan
second_number = int(input())
temp1 = first_number
temp2 = second_number

greater = max(first_number, second_number)
smallest = min(first_number, second_number)
Kmm = 1
for i in range(greater, first_number*second_number+1, greater):
    if i % smallest == 0:
        Kmm = i
        break
Bmm = int((first_number * second_number) / Kmm)
print(Bmm , Kmm)