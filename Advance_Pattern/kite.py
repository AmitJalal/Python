"""
n = 5

    * 
   ***
  ***** 
 ******* 
********* 
 *******
  *****
   ***
    * 

"""

n = int(input())
i = 1

# increasing stars row
while i <= n:
    spaces = n - i
    space = 1
    while space <= spaces:
        print(" ", end="")
        space += 1
    stars = 2 * i - 1
    star = 1
    while star <= stars:
        print("*", end="")
        star += 1

    print()
    i += 1

# decreasing stars row
i = 1
row = n - 1
while row >= 1:
    spaces = i
    space = 1
    while space <= spaces:
        print(" ", end="")
        space += 1

    stars = row * 2 - 1
    star = 1
    while star <= stars:
        print("*", end="")
        star += 1

    print()
    row -= 1
    i += 1
