# average time: 49.8ns

start = incr = 20

for j in range(20, (start/2 + 1), -1):
    for i in range(1, j+1):
        if((incr*i) % (j-1) == 0):
            incr *= i
            print(incr)
            break
