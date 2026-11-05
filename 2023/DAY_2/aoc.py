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

games = {}
max_c = {'red':12,'blue':14,'green':13}
for line in file.readlines():
    line = line.strip().split(':')
    games[int(line[0].replace('Game ',''))] = line[1]

for game in games:
    found = False
    tgm = games[game].strip().split(';')
    tmax = {'red':0,'blue':0,'green':0}
    for tsh in tgm:
        ctsh = tsh.split(',')
        for cctsh in ctsh:
            for col in max_c:
                if col in cctsh:
                    cur = re.sub(r'[^0-9]','',cctsh)
                    if int(cur) > max_c[col]:
                        found = True
                    if int(cur) > tmax[col]:
                        tmax[col] = int(cur)
    if not found:
        p1 += int(game)
    tp2 = 1
    for col in tmax:
        if tmax[col] == 0:
            print(f'{game}{games[game]}')
        else:
            tp2 *= tmax[col]
    p2 += tp2
print(f'part1: {p1}')
print(f'part2: {p2}')



