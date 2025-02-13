a = input("Enter a Number: ")
for i in range(0, int(len(a)/2)):
    if a[i] == a[-1 *(i+1)]:
        pass
    else:
        print("False")
        exit()
print("True")