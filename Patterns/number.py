n = int(input())

row = 1
while row <= n:
    col = 1
    while col <= n:
        print(row, end='')
        col += 1
    print()
    row += 1

'''
n=5 --> 
    11111
    22222
    33333
    44444
    55555
'''
