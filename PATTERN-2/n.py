n = int(input())
i = 1


while i <= n:
    spaces = 1
    while spaces <= n-i:
        print(" ", end="")
        spaces += 1
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1


'''
n=4

   1
  12
 123
1234

==============================

   n = 6

       1
      12
     123
    1234
   12345
  123456 
  
'''
