n = int(input("Enter the number:"))

i = 1
col = n*2
while i <= n:

    increasing_no = 1
    while increasing_no <= i:
        print(increasing_no, end=" ")
        increasing_no += 1

    spaces = col - (i*2)
    space = 1
    while space <= spaces:
        print(" ", end=" ")
        space += 1

    decreasing_no = i
    while decreasing_no >= 1:
        print(decreasing_no, end=" ")
        decreasing_no -= 1

    print()
    i += 1


'''
 n = 4

    1             1
    1 2         2 1
    1 2 3     3 2 1
    1 2 3 4 4 3 2 1

=============================

  n = 9

    1                                 1
    1 2                             2 1
    1 2 3                         3 2 1
    1 2 3 4                     4 3 2 1
    1 2 3 4 5                 5 4 3 2 1
    1 2 3 4 5 6             6 5 4 3 2 1
    1 2 3 4 5 6 7         7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8     8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 9 9 8 7 6 5 4 3 2 1

 
'''