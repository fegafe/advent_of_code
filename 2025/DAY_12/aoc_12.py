import time
import sys
import heapq
import collections
from collections import defaultdict

start_time = time.perf_counter()

sys.setrecursionlimit(1000000)
##some = defaultdict(int)

def print_map(mapp,mx,my):
    for y in range(my):
        for x in range(mx):
            print(mapp[y][x],end='')
        print()

file = open('example.txt','r')
file = open('input.txt','r')
p1 = 0
p2 = 0

shapes = {}
shap = True
spaces = []
for sline in file.readlines():
    line = sline.strip()
    if len(line)<1:
        continue
    if ':' in line:
        if 'x' in line:
            shap = False
        if shap:
            line = line.split(':')
            sh = line[0]
            shapes[sh] = {'shape':[],'size':0}
        else:
            line = line.split(':')
            spaces.append((line[0].strip(),[int(x) for x in line[1].strip().split()]))
    else:
        shapes[sh]['shape'].append(line)
        shapes[sh]['size'] += sum([1 if x == '#' else 0 for x in line])

# for sh in shapes:
    # print(sh)
    # for x in shapes[sh]:
        # print(x)
print(shapes)

tch = 0
for space in spaces:
    # print(space)
    mx,my = [int(x) for x in space[0].split('x')]
    tmap = [['*']*mx]*my
    # print_map(tmap,mx,my)
    tot = sum(space[1])
    px = mx // 3
    py = my // 3
    nmax = px * py
    tot2 = 0
    for i,x in enumerate(space[1]):
        tot2 += x*shapes[str(i)]['size']
    if tot2 > mx*my:
        continue
    if nmax >= tot:
        p1 += 1
        continue
    tch += 1

print(tch)

    
            # print(f'{space} {px}*{py} {px*py} {tot}')
    # print('='*30)
print(f'{tch}/{len(spaces)}')

print(f'Part1: {p1}')
print(f'Part2: {p2}')


print(f"Execution time: {(time.perf_counter() - start_time):.4f} seconds")
