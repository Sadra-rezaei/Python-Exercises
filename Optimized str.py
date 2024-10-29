x = input()
org_str = input()
org_list = list(org_str)
i = 0

while i < len(org_list) - 1:

    if org_list[i] == org_list[i + 1]:
        org_list.pop(i)
        org_list.pop(i)
        i -= 1

    else:
        i += 1

org_str = ''.join(org_list)
print(org_str)