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


print() # new b/w different o/p

row = 1
while row <= n :
    col = n 
    while col>0:
        print(col, end='')
        col-=1
    print()    
    row+=1

'''
output : n = 4

4321
4321
4321
4321

'''    