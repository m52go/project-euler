# average time: 47.9ns

ab = 0
abset = set()

for i in xrange(1, 1000):
    ab = round((1000*(-500+i))/(i-1000.0), 4) # paper/pencil
    if((ab > 0) & (ab%1 == 0)):
        abset.add(ab)

a = abset.pop(); b = abset.pop()
c = 1000 - a - b
print(a, b, c, a * b * c)
