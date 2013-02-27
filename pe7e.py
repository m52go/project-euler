average time: 50ns

import math

i = 1; n = 3 

def isPrime(n):
    n = int(n)
    if n%2 == 0: return False
    for i in xrange(3, int(math.sqrt(n))+1, 2):
        if(n%i == 0):
            return False
    return True 

while(i < 10001):
    if(isPrime(n)):
        i += 1
    n += 2

print(n-2)
