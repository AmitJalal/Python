'''
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i*i
print(sum)

'''

n = int(input())
sum = int((n*(n+1)*((2*n)+1))/6)

print(type(sum))
