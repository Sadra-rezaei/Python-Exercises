from idlelib.replace import replace
from os import remove

harf = input("ye chiz benevis: ")
harf = harf.lower()
list = []
for i in harf:
    list.append(i)
for i in list:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        list.remove(i)
new_string = ""
for i in list:
    new_string +='.'+ i
print(new_string)




