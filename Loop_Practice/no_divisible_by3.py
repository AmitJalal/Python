''' print numbers in the range of (a, b) both inclusive that are divisible by 3 '''
a = int(input())
b = int(input())

div = a % 3

if div == 1:
    a += 2

elif div == 2:
    a += 1


for ele in range(a, b+1, 3):
    print(ele)
