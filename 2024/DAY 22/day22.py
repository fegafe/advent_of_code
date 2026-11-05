import sys

def nextsn(sn):
    if sn in cache:
        return cache[sn]
    tsn = sn
    tsn = mix(64*tsn,tsn)
    tsn = prune(tsn)
    tsn = mix(tsn//32,tsn)
    tsn = prune(tsn)
    tsn = mix(tsn*2048,tsn)
    tsn = prune(tsn)
    cache[sn] = tsn
    return tsn

def mix(x,y):
    return x ^ y

def prune(tsn):
    return tsn%16777216

# file = open('example.txt','r')
file = open('input.txt','r')

sys.setrecursionlimit(1000000)

snum = {}
j = 0
for line in file.readlines():
    snum[int(line.strip())]= []
    snum[int(line.strip())].append(int(line.strip()))
# print(snum)

cache = {}

sn = 123
i = 0
# while i < 10:
    # nsn = nextsn(sn)
    # print(f'{sn}->{nsn}')
    # sn = nsn
    # i += 1

i = 0
nth = 2000
for n in snum:
    i = 0
    while i < nth:
        # print(f'{i}::{n}::{snum[n][-1]}')
        snum[n].append(nextsn(snum[n][-1]))
        i += 1
    # print(snum[n][nth])
respart1 = 0

for n in snum:
    respart1 += snum[n][nth]
print(f'{respart1 = }')

sec = {}
psec = {}
for n in snum:
    sec[n] = []
    ld = snum[n][0]
    i = 0
    psec[n] = {}
    for sn in snum[n]:
        nd = sn%10
        sec[n].append(nd-ld)
        ld = nd
        if i > 4:
            psec[n][(sec[n][-4],sec[n][-3],sec[n][-2],sec[n][-1])] = sn%10
        i += 1

# print(snum[1][:12])
# print(sec[1][:12])
# print(psec[1])
respart2 = 0
csec = {}
for n in psec:
    for sec in psec[n]:
        if sec in csec:
            csec[sec] += 1
        else:
            csec[sec] = 1
sorted_by_values = dict(sorted(csec.items(), key=lambda item: item[1], reverse=True))
# print(sorted_by_values)
maxv = 0
for secs in sorted_by_values:
    tval = 0
    for n in psec:
        if secs in psec[n]:
            tval += psec[n][secs]
    if tval > maxv:
        maxv=tval
respart2 = maxv
print(f'{respart2 = }')