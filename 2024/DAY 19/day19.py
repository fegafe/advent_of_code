import itertools
###ALWAYS SAVE YOUR WORK!!!
# file = open('example.txt','r')
file = open('input.txt','r')

def findpatt(pat):
    if pat not in solved:
        if len(pat) == 0:
            return 1
        else:
            r = 0
            for a in avai:
                if pat.startswith(a):
                    r += findpatt(pat[len(a):])
            solved[pat] = r
    return solved[pat]

avai = []
patterns = []
i = 0
for line in file.readlines():
    line = line.strip()
    if i == 0:
        for des in line.split(','):
            avai.append(des.strip())
    if i >= 2:
        patterns.append(line)
    i += 1

solved = {}
respart1 = 0
respart2 = 0
for p in patterns:
    r= findpatt(p)
    if r> 0:
        respart1 += 1      ##PART1
    respart2 += r##PART2
print(f'{respart1 =}')
print(f'{respart2 =}')