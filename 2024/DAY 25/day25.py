import sys
from itertools import combinations

# file = open('example.txt','r')
file = open('input.txt','r')

sys.setrecursionlimit(1000000)


keys = {}
lock = {}
item = {}
k = 0
l = 0
i = 0
cl = False
item[0] = []
for line in file.readlines():
    line = line.strip()
    if line == '':
        i += 1
        item[i] = []
    else:
        item[i].append(line)

# print(item)
for it in item:
    if item[it][0] == '#####':
        tlock = [0,0,-1,0,0]
        tln = 0
        for tl in item[it]:
            for i in range(len(tl)):
                if tl[i] == '#':
                    tlock[i] = tln
            tln += 1
        lock[l] = tlock.copy()
        l += 1
    if item[it][0] == '.....':
        tkeys = [0,0,0,0,0]
        tln = 0
        for tl in item[it]:
            for i in range(len(tl)):
                if tl[i] == '.':
                    tkeys[i] = 5-tln
            tln += 1
        keys[k] = tkeys.copy()
        k += 1
# print(lock)
# print(keys)

count = 0
for l in lock:
    for k in keys:
        fail = False
        for i in range(5):
            if lock[l][i]+keys[k][i] >5:
                fail = True
        if not fail:
            count += 1

print(f'{count = }') ##3663