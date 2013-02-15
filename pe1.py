def sumn(n):
    num = 0
    while num < n:
        if ((num%3)==0) or ((num%5)==0):
            print num	
            yield num
        num += 1

threefivesum = sum(sumn(1000))

print threefivesum
