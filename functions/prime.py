import math

# n=int(input())
'''
def checkPrime(n):
    end = math.sqrt(n)
    for i in range(2, int(end)+1):
        if n % i == 0:
            print("not a prime")
            break

    else:
        print("prime")
'''

# refactored

def checkPrime(n):
    end=math.sqrt(n)
    for i in range(2, int(end)+1):
        if n % i == 0:
            return False
    else : 
        return True


print(checkPrime(4))
print(checkPrime(27))
print(checkPrime(11))
print(checkPrime(17))
print(checkPrime(29))
print(checkPrime(25))
print(checkPrime(19))