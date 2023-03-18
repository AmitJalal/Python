n = int(input("Enter number: "))

i = 1

increasing_row = (n+1)//2
while i <= increasing_row:

    required_spaces = i - 1
    space = 1
    while space <= required_spaces:
        print(" ", end="")
        space += 1

    star = 1
    while star <= i:
        print("* ", end="")
        star += 1

    print()
    i += 1

decreasing_row = n//2
while decreasing_row >= 1:

    required_spaces = decreasing_row-1
    space = 1
    while space <= required_spaces:
        print(" ", end="")
        space += 1

    star = 1
    while star <= decreasing_row:
        print("* ", end="")
        star += 1

    print()
    decreasing_row -= 1

'''
 n = 7

*
 * *
  * * *
   * * * *
  * * *
 * *
* 

# =========================

Enter number: 11

*
 * *
  * * *
   * * * *
    * * * * *
     * * * * * *
    * * * * *
   * * * *
  * * *
 * *
*

# ===============================

Enter number: 21

*
 * *
  * * *
   * * * *
    * * * * *
     * * * * * *
      * * * * * * *
       * * * * * * * *
        * * * * * * * * *
         * * * * * * * * * *
          * * * * * * * * * * *
         * * * * * * * * * *
        * * * * * * * * *
       * * * * * * * *
      * * * * * * *
     * * * * * *
    * * * * *
   * * * *
  * * *
 * *
*

'''
