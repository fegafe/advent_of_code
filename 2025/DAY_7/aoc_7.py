import time
import sys
import heapq
import collections
from collections import defaultdict

start_time = time.perf_counter()

sys.setrecursionlimit(1000000)
#some = defaultdict(int)
checked = {}
def cw(x,y):
    print(f'checking: ({x},{y})')
    if (x,y) in checked:
        return checked[(x,y)]
    if y >= my-1:
        return 1
    if x+1 in tchs[y+2] and x-1 in tchs[y+2]:
        checked[(x,y)] = cw(x+1,y+2) + cw(x-1,y+2)
    elif x+1 in tchs[y+2]:
        checked[(x,y)] = cw(x+1,y+2)
    elif x-1 in tchs[y-2]:
        checked[(x,y)] = cw(x-1,y+2)
    return checked[(x,y)]

file = open('example.txt','r')
file = open('input.txt','r')
p1 = 0
p2 = 0
y  = 0
tch  = {}
cmap = []
nmap = []
for sline in file.readlines():
    line = sline.strip()
    cmap.append([0]*len(line))
    nmap.append(line)
    if y == 0:
        for x,v in enumerate(line):
            if v == 'S':
                sp     = x
                tch[x] = 1
                cmap[y][x] = 1
    else:
        for x,v in enumerate(line):
            if v == '^':
                if x in tch:
                    if tch[x] > 0:
                        p1 += 1
                        tch[x+1] = 1
                        tch[x-1] = 1
                        tch[x]   = 0
    y += 1
my = y-1

for y in range(1,len(cmap)):
    for x in range(len(cmap[0])-1):
        if nmap[y][x] == '^':
            cmap[y][x+1] = cmap[y][x+1] + cmap[y-1][x]
            cmap[y][x-1] = cmap[y][x-1] + cmap[y-1][x]
        else:
            cmap[y][x] = cmap[y-1][x] + cmap[y][x]

p2 = sum(cmap[-2])
print(f'Part2: {p1}')
print(f'Part2: {p2}')


print(f"Execution time: {(time.perf_counter() - start_time):.4f} seconds")


##TOOLOW
##3216