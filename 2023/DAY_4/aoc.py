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

cards = {}
infile  = []
for line in file.readlines():
    sline   = line.strip().split(':')
    card   = sline[0].strip().split(' ')
    cards[int(card[-1].strip())] = 1
    infile.append(line)

for line in infile:
    sline   = line.strip().split(':')
    points = 0
    card   = sline[0].strip().split(' ')
    ccard  = int(card[-1].strip())
    other  = sline[1].strip().split('|')
    wnumstr   = other[0].strip().split(' ')
    mynumstr  = other[1].strip().split(' ')
    wnums = []
    for wns in wnumstr:
        if wns.strip().isdigit():
            wnums.append(int(wns.strip()))
    mynums = []
    for mns in mynumstr:
        if mns.strip().isdigit():
            mynums.append(int(mns.strip()))
     
    for num in mynums:
        if num in wnums:
            points += 1
    if points > 0:
        p1 += 2**(points-1)
    for i in range(1,points+1):
        cards[ccard+i] += cards[ccard]

    # print(f'{ccard}:{points}||{cards}')

print(f'part1: {p1}')
for c in cards:
    p2 += cards[c]
print(f'part2: {p2}')

