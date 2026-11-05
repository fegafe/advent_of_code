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

cmap = []
maxx = 0

for line in file.readlines():
    line = line.strip()
    cmap.append(line)
    cmax = len(line)
    if cmax > maxx:
        maxx = cmax

maxy = len(cmap)
gear = {}
for y in range(maxy):
    x = 0
    while x < maxx:
        if cmap[y][x].isdigit():
            cstr = cmap[y][x:]
            match = re.search('\d+',cstr)
            val = int(cstr[match.start():match.end()])
            found = False
            nminx = x-1 if x-1>=0  else x
            nmax  = x+match.end()+1 if (x+match.end()+1 <= maxx) else maxx
            if y-1 >=0:
                for nx in range(nminx,nmax):
                    if cmap[y-1][nx] not in ['0','1','2','3','4','5','6','7','8','9','.']:
                        found = True
                        if cmap[y-1][nx] == '*':
                            if (y-1,nx) not in gear:
                                gear[(y-1,nx)] = []
                            gear[(y-1,nx)].append(val)
            if y+1 < maxy:
                for nx in range(nminx,nmax):
                    if cmap[y+1][nx] not in ['0','1','2','3','4','5','6','7','8','9','.']:
                        found = True
                        if cmap[y+1][nx] == '*':
                            if (y+1,nx) not in gear:
                                gear[(y+1,nx)] = []
                            gear[(y+1,nx)].append(val)
            if cmap[y][nminx] not in ['0','1','2','3','4','5','6','7','8','9','.']:
                found = True
                if cmap[y][nminx] == '*':
                    if (y,nminx) not in gear:
                        gear[(y,nminx)] = []
                    gear[(y,nminx)].append(val)
            if cmap[y][nmax-1] not in ['0','1','2','3','4','5','6','7','8','9','.']:
                found = True
                if cmap[y][nmax-1] == '*':
                    if (y,nmax-1) not in gear:
                        gear[(y,nmax-1)] = []
                    gear[(y,nmax-1)].append(val)
            if found:
                p1 += val
            # else:
                # print(f'not {val}|{x}|{x + match.end()}')
            x = x + match.end()
        else:
            x += 1
        # print(cmap[y][x],end='')
    # print()
    
print(f'part1: {p1}')

for gea in gear:
    if len(gear[gea]) == 2:
        p2 += gear[gea][0]*gear[gea][1]
    # else:
        # print(f'{gea}->{gear[gea]}')
print(f'part2: {p2}')

