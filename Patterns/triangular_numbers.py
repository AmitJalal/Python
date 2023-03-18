n = int(input())

''' pattern 1 -->'''

row = 1
while row <= n:
    col = 0
    while col < row:
        print(row + col, end=' ')
        col += 1
    print()
    row += 1

'''
 output : n = 4
 
    1
    2 3
    3 4 5
    4 5 6 7

'''
#######################################################################

print()

''' pattern 2 --> '''

row = 1

while row <= n:
    col = 1
    while col <= row:
        print(col, end=' ')
        col += 1
    print()
    row += 1

'''
output : n = 5

    1
    1 2
    1 2 3
    1 2 3 4

'''

#################################################################################

print()

''' pattern 3 --> '''


row = 1
num = 1
while row <= n:
    col = 1
    while col <= row:
        print(num, end =' ')
        num+=1
        col+=1
    print()    
    row+=1

'''  
output : n = 4

    1
    2 3
    4 5 6
    7 8 9 10

'''

###########################################################