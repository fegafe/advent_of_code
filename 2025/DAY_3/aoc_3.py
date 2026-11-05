import time
import sys
import heapq
import collections
from collections import defaultdict

###09:11
###09:21
###09:46
start_time = time.perf_counter()

sys.setrecursionlimit(1000000)
##some = defaultdict(int)

file = open('example.txt','r')
file = open('input.txt','r')
p1 = 0
p2 = 0

for sline in file.readlines():
    line = sline.strip()
    ##PART1
    ind  = line.index(max(line[:-1]))
    p1 += int(max(line[:-1]))*10 + int(max(line[ind+1:]))
    ##PART2
    li = 0
    dd = [0]*12
    for i in range(12,0,-1):
        # print(f'{li} -- {-1*i+1}')
        if i > 1:
            culine = line[li:(-1*i+1)]
            max_v    = max(culine)
        else:
            culine = line[li:]
            max_v    = max(culine)
        li       = li + culine.index(max_v)+1
        dd[12-i] = max_v
        # print(f'{max_v} at {li}')
    # print("".join(dd))
    p2 += int("".join(dd))
    
print(f'Part1: {p1}')
print(f'Part2: {p2}')

end_time = time.perf_counter()
print(f"Execution time: {(end_time - start_time):.4f} seconds")
