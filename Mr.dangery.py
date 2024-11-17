from http.cookiejar import uppercase_escaped_char

n = int(input())
i = 0
temp_List = []
mr_Danger_List = []

while i < n:
    temp = input()
    temp_List.append(temp)
    i += 1

flag = 1
for i in temp_List:
    if flag == 1:
        if i != "CAPS":
            mr_Danger_List.append(i)
        else:
            flag = 0
    else:
        if i != "CAPS":
            i = i.upper()
            mr_Danger_List.append(i)
        else:
            flag = 1

mr_Danger_String = ''.join(mr_Danger_List)
print(mr_Danger_String)