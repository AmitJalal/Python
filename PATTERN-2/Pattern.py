# c = ord("A") + 5
# print(chr(c))

n = int(input())

start_letter = ord("A") + n 

# print(chr(start_letter))
i = 1

while i<=n:
    j=0
    while j<i:
        print(chr(start_letter -  i + j), end ="")
        j+=1
    print()
    i += 1


'''
o/p :
 n = 5
    E
    DE
    CDE
    BCDE
    ABCDE

n = 8
    H
    GH
    FGH
    EFGH
    DEFGH
    CDEFGH
    BCDEFGH
    ABCDEFGH

'''