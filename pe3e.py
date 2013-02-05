# average time: 51.5ns for 600851475143
# basic sieves implementation results in 9 orders of magnitude improvement

num = 600851475143 # input("Number: ")

d = 2
factors = []

while num > 1:
    while(num % d == 0):
        factors.append(d)
        num = num / d
    d += 1

print(factors[-1])
