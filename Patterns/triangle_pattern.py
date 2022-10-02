
''' printing stars in triangle pattern in increasing order '''

n = int(input())

row = 1

while row <= n:
    col = 1
    while col <= row:
        print('*', end='')
        col += 1
    print()
    row += 1

'''
output : n = 4 

*
**
***
****

'''

#########################################################################

print()

''' printing stars in triangle pattern in decreasing order '''

row = n

while row > 0:
    col = row
    while col > 0:
        print('*', end='')
        col -= 1
    print()
    row -= 1

'''
output: n = 4 

****
***
**
*

'''
###########################################################################

print()  # empty line for new input

''' printing nummbers in decreasing order in triangle pattern '''


row = n
while row > 0:
    col = row
    while col > 0:
        print(col, end='')
        col -= 1
    print()
    row -= 1


'''
output for n = 4

4321
321
21
1

'''
##########################################################################

print()  # print new line for  new outputs

''' printing the triangle with as many coloumns wtih the increase in row '''

row = 1
while row <= n:
    col = 1
    while col <= row:
        print(row, end='')
        col += 1
    print()
    row += 1

'''
output : n = 4

1
22
333
4444

'''
