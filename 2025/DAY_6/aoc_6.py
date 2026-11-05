import time
import sys
import heapq
import collections
import re
from collections import defaultdict

start_time = time.perf_counter()

sys.setrecursionlimit(1000000)
##some = defaultdict(int)

file = open('example.txt','r')
file = open('input.txt','r')
p1 = 0
p2 = 0
lines = []
for sline in file.readlines():
    line  = sline.replace('\n','')
    if '+' not in line:
        lines.append(line)
    else:
        top = line

cc = []
for i,x in enumerate(top):
    if x in ['+','*']:
        cc.append(i)

# print(top)
# print(cc)

rows = []
for line in lines:
    lc = 0
    crow = []
    for d in cc[1:]:
        crow.append(line[lc:d-1])
        lc = d
    crow.append(line[lc:])
    rows.append(crow)

# print(lines)
# print(rows)
cols = []
for i in range(len(rows[0])):
    cols.append([])
for row in rows:
    for i,v in enumerate(row):
        cols[i].append(v)

# print(cols)
# print(op)

# for i,col in enumerate(cols):
    # if op[i] == '+':
        # p1 +=sum(col)
    # elif op[i] == '*':
        # res = 1
        # for x in col:
            # res *= x
        # p1 += res
# print(f'Part1: {p1}')
op = top.split()
# print(op)
for i,col in enumerate(cols):
    # print(col)
    maxl =  len(col[0])
    ncol = []
    for j in range(maxl):
        cval = ''
        for t in col:
            if t[maxl-j-1] != ' ':
                cval = cval + str(int(t[maxl-j-1]))
        ncol.append(int(cval))
    # print(ncol)
    if op[i] == '+':
        # print(f'+ {ncol}')
        p2 +=sum(ncol)
    elif op[i] == '*':
        # print(f'* {ncol}')
        res = 1
        for x in ncol:
            res *= x
        p2 += res

print(f'Part2: {p2}')


print(f"Execution time: {(time.perf_counter() - start_time):.4f} seconds")
