# average time: 48.2ns

# open file with data, store in h
with open('pe11fig.txt', 'r') as f:
    h = [int(i) for line in f for i in line.split(' ')]

# make rows
hi = []
for i in range(1, 21):
    hi.append(h[(i*20 - 20):i*20])

# make columns
ci = []
for i in range(20):
    ci.append([hi[j][i] for j in range(20)])

global highnums
global highprod
nums = [0, 0, 0, 0] 
prod = 0
highnums = 0
highprod = 0

# take three numbers and compare to highest known
def compare(nums):
    global highnums; global highprod
    prod = nums[0] * nums[1] * nums[2] * nums[3]
    if prod > highprod:
        highnums = nums[:]; highprod = prod
    
# find highest products in hi and ci (only moving up+down)
def rook(hi):
    for i in range(len(hi)):
        for j in range(17):
            for k in range(0, 4):
                nums[k] = hi[i][j+k]
            compare(nums)

# find highest products diagonally
def bishop():
    callsingle([0,19], [19,0], 1, 1, 2, -1)
    callsingle([16,19], [19,16], 0, 3, 0, -1)
    callsingle([0,16], [3,19], 1, 2, 0, 1)
    callsingle([16,0], [19,3], 0, 4, -1, 1)

# refactored code from bishop to minimize repitition
def callsingle(i, j, iwhile, corner, limit, jop):
    jwhile = 1 if(iwhile == 0) else 0
    while(i[iwhile] > limit):
        single(traverse(i, j, corner))
        i[iwhile] -= 1; j[jwhile] += jop
    
# traverse single array; yes, it is a little repetitive
def single(arr):
    for j in range(len(arr) - 4):
        for k in range(0, 4):
            nums[k] = arr[j+k]
        compare(nums)

# traverse diagonal row
def traverse(i, j, corner):
    start = i[:]; end = j[:]
    diagarr = []

    if corner == 1 or corner == 3:
        x = 1; y = -1
    else:
        x = 1; y = 1
    
    while(start[0] <= end[0]):
        diagarr.append(hi[start[0]][start[1]])
        start[0] += x; start[1] += y

    return diagarr

rook(hi)
rook(ci)
bishop()

print(highnums, highprod)
