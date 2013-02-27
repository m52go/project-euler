# average time: 180s, way over 60s maximum...

i = j = k = 3
factors = []
primes = 1  #starting at 3

while(primes < 10001):
    while(i > 1):
        while(i%j == 0):
            factors.append(j)
            i /= j
        if(len(factors) > 1):
            break
        j += 2
    if(len(factors) == 1):
        primes += 1
    factors = []; k += 2; i = k; j = 3

print(k-2)
