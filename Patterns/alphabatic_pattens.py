n = int(input())

alpha = ord('A')
row = 1
while row <= n:
    col = 0
    while col <= n:
        print(chr(alpha+col), end=' ')
        col += 1
    print()
    row += 1


''' 
output for n = 4 

A B C D E
A B C D E
A B C D E
A B C D E

'''    
print()

####################################################

alpha = ord('A')
row = 1

while row <= n:
    col = 0
    while col <= n:
        print(chr(alpha), end=' ')
        alpha+=1
        col += 1
    print()
    row += 1

'''
output : n = 4

    A B C D E
    F G H I J
    K L M N O
    P Q R S T

'''   

print()

###################################################################