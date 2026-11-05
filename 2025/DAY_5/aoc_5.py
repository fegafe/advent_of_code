import time
import sys
import heapq
import collections
from collections import defaultdict

start_time = time.perf_counter()

sys.setrecursionlimit(1000000)
##some = defaultdict(int)

# file = open('example.txt','r')
file = open('input.txt','r')
p1 = 0
p2 = 0

found = False
ing    = []
ranges = []
for sline in file.readlines():
    line = sline.strip()
    if line == '':
        found= True
        continue
    if not found:
        low  = line.split('-')[0]
        high = line.split('-')[1]
        ranges.append((int(low),int(high)))
    else:
        ing.append(int(line))

print(f"Lo Execution time: {(time.perf_counter() - start_time):.4f} seconds")
start_time = time.perf_counter()

sranges = sorted(ranges, key=lambda x:x[0],reverse =  False)

for i in ing:
    for r in sranges:
        if  r[0] <= i <= r[1]:
            p1 += 1
            break

print(f'Part1: {p1}')
print(f"P1 Execution time: {(time.perf_counter() - start_time):.4f} seconds")
start_time = time.perf_counter()

nranges = []
for r in sranges:
    nt = r
    for nr in nranges:
        if r[0] <= nr[1]:
            nt = (nr[0],max(r[1],nsr[1]))
            nranges.remove(nr)
            break
    nranges.append(nt)

for r in nranges:
    p2 += r[1]-r[0] + 1

print(f'Part2: {p2}')
print(f"P2 Execution time: {(time.perf_counter() - start_time):.4f} seconds")
