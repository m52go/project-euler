# average time: 44.4ns

import math

def isPrime(n):
     n = int(n)
     if n%2 == 0: return False
     for i in xrange(3, int(math.sqrt(n))+1, 2):
         if(n%i == 0):
             return False
     return True

n = 3
sum = 2

while(n < 2000000):
    if(isPrime(n)):
        sum += n
    n += 2

print(sum)
