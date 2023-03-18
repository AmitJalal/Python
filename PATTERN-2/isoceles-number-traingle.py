n = int(input())

i = 1

while i <= n:

    spaces = 1
    while spaces <= n-i:
        print(" ", end="")
        spaces += 1

    count = 1
    integers_per_row = i + i - 1
    while count <= i:
        print(count, end="")
        count += 1
        
    count -= 1
    left_integers = integers_per_row - count
    while left_integers > 0:
        print(left_integers, end="")
        left_integers -= 1
    print()
    # print(integers_per_row, left_integers, count)
    i += 1


'''
n = 4

       1
      121
     12321
    1234321

====================================

n = 7

      1
     121
    12321
   1234321
  123454321
 12345654321
1234567654321

'''
