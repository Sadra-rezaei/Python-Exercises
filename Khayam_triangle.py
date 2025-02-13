n = int(input()) #n = تعداد سطر های مثلث
# if n < 1 or n > 10:
#     print("Error")
#     exit()
list_1 = [1]
print(1)
for count in range(1, n):
    list_2 = list_1 + [0]
    for i in range(count):
        list_2[i + 1] += list_1[i]
        new_str = ""
        for adad in list_2:
            new_str += str(adad) + " " #اینجا لیست را به str تبدیل میکنم
    print(new_str)
    list_1 = list_2