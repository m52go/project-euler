start = 999999
oc = 10010      # outer counter
ic = 1100       # inner counter

for i in range(0, 10):
    for j in range(0, 10):
        num = start - (oc*i) - (ic*j)
        for k in range(999, 100, -1):
            if(num%k == 0):
                if(num/k < 999):
                    print(k, num/k, num)
