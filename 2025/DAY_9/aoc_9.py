import time
import sys
import heapq
import collections
from collections import defaultdict

def print_map(tp = None):
    for y in range(miny-1,my+2):
        for x in range(minx-1,mx+2):
            if (x,y) in gt:
                c = 'X'
            elif (x,y) in tm:
                c = '#'
            else:
                c = '.'
            if tp:
                if (x,y) in tp:
                    c = tp.index((x,y))+1
            print(c,end='')
        print()

def print_map_2(pp):
    miny = min(pp[0][1],pp[1][1])
    my   = max(pp[0][1],pp[1][1])
    minx = min(pp[0][0],pp[1][0])
    mx   = max(pp[0][0],pp[1][0])
    for y in range(miny-1,my+2):
        for x in range(minx-1,mx+2):
            if (x,y) in gt:
                c = 'X'
            elif (x,y) in tm:
                c = '#'
            else:
                c = '.'
            if pp:
                if (x,y) in pp:
                    c = 'O'
            print(c,end='')
        print()

start_time = time.perf_counter()
sys.setrecursionlimit(1000000)

file = open('example.txt','r')
file = open('input.txt','r')
p1 = 0
p2 = 0

tm = []
gt = []
cx = []
cy = []
mx = 0
my = 0
minx = sys.maxsize
miny = sys.maxsize
for sline in file.readlines():
    line = sline.strip()
    x,y =[int(i) for i in line.split(',')]
    tm.append((x,y))
    if y > my:
        my = y
    if x > mx:
        mx = x
    if y < miny:
        miny = y
    if x < minx:
        minx = x
# print_map()

# print(len(tm))

heap = []
for i,pi in enumerate(tm):
    if i+1 < len(tm):
        for pj in tm[i:]:
            narea = (abs(pi[0] - pj[0]) + 1)*(abs(pi[1] - pj[1]) + 1)
            heapq.heappush(heap,(-1*narea,(pi,pj)))
            if pi[1] == pj[1]:
                for x in range(pi[0],pj[0]+1):
                    gt.append((x,pi[1]))
            if pi[0] == pj[0]:
                for y in range(pi[1],pj[1]):
                    gt.append((pi[0],y))
                
                
# print_map()

print(f'Part1: {-1*heap[0][0]}')
print(f"Execution time P1: {(time.perf_counter() - start_time):.4f} seconds")

def check(pk,pl):
    check = False
    fmin  = False
    fmax  = False
    ##check pk
    if pk in tm:
        check = True
    else:
        for p in gt:
            if p[0] == pk[0]:
                if pk[1] <= p[1]:
                    fmin = True
                if pk[1] >= p[1]:
                    fmax = True
        check = fmin and fmax
    fmin  = False
    fmax  = False
    if pl in tm:
        check = check and True
    else:
        for p in gt:
            if p[0] == pl[0]:
                if pl[1] <= p[1]:
                    fmin = True
                if pl[1] >= p[1]:
                    fmax = True
        check = check and fmin and fmax
    return check


heap = []
for i,pi in enumerate(tm):
    if i+1 < len(tm):
        for pj in tm[i:]:
            narea = (abs(pi[0] - pj[0]) + 1)*(abs(pi[1] - pj[1]) + 1)
            pk = (pi[0],pj[1])
            pl = (pj[0],pi[1])
            if check(pk,pl):
                # print_map([pi,pj,pk,pl])
                heapq.heappush(heap,(-1*narea,(pi,pj)))
    if i%10 == 0:
        print(f'{i}/{len(tm)} curr: {-1*heap[0][0]} {(time.perf_counter() - start_time):.4f} seconds')
        # print_map_2(heap[0][1])
        
print(f'Part2: {-1*heap[0][0]}')
# print_map_2(heap[0][1])

# print_map()

###TOO HIGH
###4763640204
###4594552575
###1960557702
###1511881770
##62343589
print(f"Execution time: {(time.perf_counter() - start_time):.4f} seconds")
