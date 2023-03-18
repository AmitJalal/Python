n = int(input("enter no. of rows(odd no.)"))

i = 1
first_half_rows = ((n+1)//2)
while i <= first_half_rows:

    space = 1
    while space <= first_half_rows-i:
        print(" ", end=" ")
        space += 1

    stars_count = 2*i - 1
    start = 1
    while start <= stars_count:
        print("*", end=" ")
        start += 1

    print()
    i += 1

second_half_rows = n//2
i = second_half_rows

while i >= 1:

    space_count = second_half_rows - (i-1)
    space = 1
    while space <= space_count:
        print(" ", end=" ")
        space += 1

    stars_count = 2*i - 1
    star = 1
    while star <= stars_count:
        print("*", end=" ")
        star += 1

    print()
    i -= 1


'''
  n = 11
  
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
    * * * * * * * * *
      * * * * * * *
        * * * * *
          * * *
            *

'''