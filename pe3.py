# average time: 59s for 600851475143

def get_lpf(num):
    ufl = long(num/2 + 1)    # upper factor limit
    lpf = test_factors(num, long(num/2 + 1)    # largest prime factor
    print("Largest prime factor: {}".format(lpf))

def test_factors(num, ufl):
    i = 1
    while i > ufl:
        if(num % i == 0):
            factor = long(num / i)
            prime = long(check_prime(factor))
            if prime is True:
                return factor
        i += 1
    else:
        return 1

def check_prime(num):
    i = 2
    while i < (num/2 + 1):
        if(num % i == 0):
            return False
        i += 1
    else:
        return True 

# reason for while loops: integers got too big for range() and xrange()
# also tried recursion but exceeded recursion limit
