import time
import sys
import heapq
import collections
from collections import defaultdict

start_time = time.perf_counter()

sys.setrecursionlimit(1000000)
##some = defaultdict(int)

file = open('example.txt','r')
file = open('input.txt','r')
p1 = 0
p2 = 0

rmap = []
dirs = [(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0)]
pp = []
y = 0
for sline in file.readlines():
    line = sline.strip()
    rmap.append(list(line))
    for x,v in enumerate(list(line)):
        if v == '@':
            pp.append((y,x))
    y += 1
maxx = len(rmap[0])
maxy = len(rmap)

trm = {}
i = 0
tr = sys.maxsize

print(f"Prep time: {(time.perf_counter() - start_time):.4f} seconds")

while tr > 0:
    trm[i] = []
    for p in pp:
        cc = 0
        rem = []
        for d in dirs:
            nx = p[1] + d[1]
            ny = p[0] + d[0]
            if 0 <= nx < maxx:
                if 0 <= ny < maxy:
                    if rmap[ny][nx] == '@':
                        cc += 1
        if cc < 4:
            trm[i].append(p)
    tr = len(trm[i])
    for p in trm[i]:
        rmap[p[0]][p[1]] = '.'
        pp.remove(p)
    i += 1

p1 = len(trm[0])
p2 = sum([len(trm[x]) for x in trm])
print(f'Part1: {p1}')
print(f'Part2: {p2}')

print(f"Execution time: {(time.perf_counter() - start_time):.4f} seconds")
