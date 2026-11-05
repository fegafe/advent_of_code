import sys
import heapq
import collections
from collections import defaultdict
import re

sys.setrecursionlimit(1000000)
##some = defaultdict(int)
file = open('example.txt','r')
file = open('input.txt','r')
p1 = 0
p2 = 0

values = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,"nine":9,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

i=0
for line in file.readlines():
    line = line.strip()
    cur = re.sub(r'[^0-9]','',line)
    if len(cur)>0:
        p1 += int(cur[0]+cur[-1])
    cmin_index = sys.maxsize
    cmax_index = 0
    for val in values:
        if line.find(val)>=0:
            index = line.find(val)
            if index <= cmin_index:
                cmin_index = index
                lval = values[val]
            tmax = -1
            while line.find(val,tmax+1)>=0:
                tmax = line.find(val,tmax+1)
                if tmax >= cmax_index:
                    cmax_index = tmax
                    rval = values[val]
    # print(f'{val}|{index}|{cmax_index}')
    p2 += lval*10+rval
    i += 1
    # if i<100:
        # print(f'{line}|{lval}{rval}')

print(f'part1: {p1}')
print(f'part2: {p2}')



