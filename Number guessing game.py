import random
a = 0
b = 100
hads = random.randrange(a + 1, b)
print(hads)
javab = input("Bego b or k or d: ")
while javab != 'd':
    if javab == 'b':
        a = hads
        hads = random.randrange(a + 1, b)
        print(hads)
        javab = input("Bego b or k or d: ")
    elif javab == 'k':
        b = hads
        hads = random.randrange(a + 1, b)
        print(hads)
        javab = input("Bego b or k or d: ")
if javab == 'd':
    print(" AFARINNNNNN "+ str(hads) +" RO PEIDA KARDI")