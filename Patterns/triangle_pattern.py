
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

''' printing stars in triangle pattern in decreasing order '''

print()
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

''' printing nummbers in decreasing order in triangle pattern '''

print()  # empty line for new input

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

''' printing the triangle with as many coloumns wtih the increase in row '''
print()  # print new line for  new outputs

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
