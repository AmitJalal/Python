n = int(input())

i = 1

while i <= n:

    spaces = 1
    while spaces <= n-i:
        print(" ", end="")
        spaces += 1

    star = 1
    while star <= i:
        print("*", end="")
        star += 1

    print()
    i += 1


'''
n = 4

   *
  **
 ***
****

===========================

    n = 8

       *
      **
     ***
    ****
   *****
  ******
 *******
********

'''
