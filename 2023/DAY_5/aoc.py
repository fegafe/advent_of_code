import sys
import heapq
import collections
from collections import defaultdict
import re

sys.setrecursionlimit(1000000)
##some = defaultdict(int)
file = open('example.txt','r')
# file = open('input.txt','r')
p1 = 0
p2 = 0

maps = {}

for line in file.readlines():
    sline   = line.strip().split()
    if len(sline) > 0:
        if sline[0] == 'seeds:':
            seeds = list(map(int, sline[1:]))
        elif sline[1] == 'map:':
            cmap = sline[0]
            maps[cmap] = []
        elif sline[0].isdigit():
            maps[cmap].append(list(map(int, line.strip().split())))

nmap = {}
for cm in maps:
    keys = cm.split('-')
    dest    = {}
    nmap[keys[0]] = {'to':keys[2],'ranges':maps[cm]}

# print(seeds)
# print(nmap)

locs   = []
for seed in seeds:
    key    = 'seed'
    source = seed
    while key != 'location':
        found = False
        for r in nmap[key]['ranges']:
            if r[1] <= source <= r[1]+r[2]:
                found = True
                source = r[0] + (source - r[1])
                break
        if not found:
            source = source
        key    = nmap[key]['to']
    locs.append(source)

p1 = min(locs)
print(f'part1: {p1}')

iseq = []

for i in range(0,len(seeds)-1,2):
    iseq.append((seeds[i],seeds[i]+seeds[i+1]-1))

print(sorted(iseq,key=lambda x:x[0]))

for key in nmap:
    for r in nmap[key]['ranges']:
        
# def segment(lseq,cseq):
    
    # return nseq

print(f'part2: {p2}')