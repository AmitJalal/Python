n = int(input())

i = 1

while i <= n:

    spaces = 1
    while spaces <= n-i:
        print(" ", end=" ")
        spaces += 1

    start = 1
    count = i
    while start <= i:
        print(count, end=" ")
        count += 1
        start += 1

    count -= 2
    start = 0
    while start < i - 1:
        print(count, end=" ")
        count -= 1
        start += 1

    print()
    i += 1

'''
 n = 4

      1
    2 3 2
  3 4 5 4 3
4 5 6 7 6 5 4

================================

  n = 5

              1
            2 3 2
          3 4 5 4 3
        4 5 6 7 6 5 4
      5 6 7 8 9 8 7 6 5
    6 7 8 9 10 11 10 9 8 7 6
'''




# ================ other way of printing this pattern ================

n = int(input())

i = 1

while i <= n:

    spaces = 1
    while spaces <= n-i:
        print(" ", end=" ")
        spaces += 1

    increasing_no = i
    total_ele = 1
    while total_ele <= i:
        print(increasing_no, end=" ")
        total_ele += 1
        increasing_no += 1

    decreasing_no = 2*i-2
    total_ele = 1
    while total_ele <= i-1:
        print(decreasing_no, end=" ")
        decreasing_no -= 1
        total_ele += 1

    print()
    i += 1
