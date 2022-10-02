''' printing square patterns of stars '''

n = int(input())

row = 0

while row < n:
    col = 0
    while col < n:
        print('*', end='')
        col += 1
    print()
    row += 1

'''
n = 4 --> 
        ****   
        ****
        ****
        ****

n = 2 -->
        **
        **
'''
