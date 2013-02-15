# average time: 55.1ns

sumsq = sqsum = 0

for i in range(1, 101):
    sumsq += i**2
    sqsum += i

sqsum **= 2

print(sqsum - sumsq) 
