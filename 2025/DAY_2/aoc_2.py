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

ranges    = []
for sline in file.readlines():
    line = sline.strip().split(',')
    for l in line:
        r = l.split('-')
        ranges.append([int(r[0]),int(r[1])])

for r in ranges:
    for i in range(r[0],r[1]+1):
        val = str(i)
        lv  = len(val)
        hv = lv // 2
        if lv%2 == 0:
            if val[:hv] == val[hv:]:
                p1 += i
        for j in range(1,hv+1):
            if val[:j]*(lv//j) == val:
                p2 += i
                break

print(f'Part1: {p1}')
print(f'Part2: {p2}')

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")
