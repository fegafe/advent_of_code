import sys
import heapq
import collections
from collections import defaultdict

sys.setrecursionlimit(1000000)
##some = defaultdict(int)

file = open('input.txt','r')

# file = open('example.txt','r')
c   = 50
p1  = 0
p2  = 0
for line in file.readlines():
    line = line.strip()
    if line[0] == 'R':
        c   = c + int(line[1:])
        p2 += c // 100
        c   = c%100
    elif line[0] == 'L':
        if c == 0:
            p2 -= 1
        c = c - int(line[1:])
        while c < 0:
            c  += 100
            p2 += 1
        if c == 0:
            p2 += 1
    ###PART 1
    if c == 0:
        p1 += 1
print(f'part1: {p1}')
print(f'part2: {p2}')
