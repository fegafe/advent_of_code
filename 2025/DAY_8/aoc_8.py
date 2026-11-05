import time
import sys
import heapq
import collections
from collections import defaultdict
# import math
# import numpy as np

start_time = time.perf_counter()

sys.setrecursionlimit(1000000)
##some = defaultdict(int)

# file = open('example.txt','r')
# n = 10

file = open('input.txt','r')
n = 1000

p1 = 1
p2 = 0
pp = []

for sline in file.readlines():
    line = sline.strip()
    x,y,z = [int(x) for x in line.split(',')]
    pp.append((x,y,z))

s =len(pp)
heap = []

for i in range(s):
    for j in range(i+1,s):
        d = (pp[i][0]-pp[j][0])**2+(pp[i][1]-pp[j][1])**2+(pp[i][2]-pp[j][2])**2
        if d > 0:
            heapq.heappush(heap,(d,(i,j)))

print(f'found distances {(time.perf_counter() - start_time):.4f} seconds')

circuits = []
for i in range(len(heap)):
    points = heapq.heappop(heap)[1]
    found = False
    cc = []
    for c in range(len(circuits)):
        if points[0] in circuits[c]:
            cc.append(c)
            found = True
        elif points[1] in circuits[c]:
            cc.append(c)
            found = True
    if not found:
        circuits.append([points[0],points[1]])
    else:
        if len(cc)>1:
           for x in circuits[cc[1]]:
               if x not in circuits[cc[0]]:
                   circuits[cc[0]].append(x)
           circuits.pop(cc[1])
        else:
           if points[0] not in circuits[cc[0]]:
               circuits[cc[0]].append(points[0])
           if points[1] not in circuits[cc[0]]:
               circuits[cc[0]].append(points[1])
        if i == n-1:
            scircuits = sorted(circuits,key=len,reverse=True)
            for i in range(3):
                p1 = p1 * len(scircuits[i])
            print(f'Part1: {p1}')
        if len(circuits) == 1:
            if len(circuits[0]) == len(pp):
                p2 = pp[points[0]][0]*pp[points[1]][0]
                print(f'Part2: {p2}')
                print(f"Execution time: {(time.perf_counter() - start_time):.4f} seconds")
                exit()

print(f"Execution time: {(time.perf_counter() - start_time):.4f} seconds")
