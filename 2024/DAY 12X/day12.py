def region(x0,y0):
    global border
    reg = []
    reg.append((x0,y0))
    seen.append((x0,y0))
    per = 0
    border = set()
    for nxy in reg:
        x = nxy[0]
        y = nxy[1]
        for d in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx = x + d[0] 
            ny = y + d[1]
            if 0 <= nx <= mxx and 0 <= ny <= mxy:
                if garden[ny][nx] == garden[y0][x0]:
                    if (nx,ny) not in reg:
                        reg.append((nx,ny))
                        seen.append((nx,ny))
                else:
                    per += 1
                    # if (x,y) not in border:
                    tbo = borderpoints(x,y,d)
                    for ttbo in tbo:
                        border.add(ttbo)
            else:
                per += 1
                # if (x,y) not in border:
                tbo = borderpoints(x,y,d)
                for ttbo in tbo:
                    border.add(ttbo)
    print(border)
    printgarden(border)
    remsimbor(border)
    # printgarden(border)
    print(f'{garden[y0][x0]}::{len(reg)}::{per}')
    return {'p':per,'a':len(reg),'plants':reg}

def remsimbor(border):
    sidex = 0
    
    for y in range(mxy+2):
        x = 0
        while x <= mxx+2:
            if (x,y) in border:
                print(x,y)
                sidex += 1
                x += 1
                while (x,y) in border:
                    x += 1
                break
            x += 1
    print(sidex)
    
def printgarden(border):
    for j in range(mxy+2):
        for i in range(mxx+2):
            if (i,j) in border:
                print('+',end='')
            else:
                print(' ',end='')
        print('')

def borderpoints(x,y,d):
    if d == (1,0):
        return[(x+1,y),(x+1,y+1)]
    if d == (-1,0):
        return[(x,y),(x,y+1)]
    if d == (0,1):
        return[(x,y+1),(x+1,y+1)]
    if d == (0,-1):
        return[(x,y),(x+1,y)]

def addv(x,y):
    return (x[0]+y[0],x[1]+y[1])

def sides_c(reg):
    sides = 0
    for b in border:
        # print(b)
        for d in border[b]:
            if border[b][d] == 1:
                sides += 1
            for b2 in border:
                if addv(b,d) == b2:
                    print(b2)
                    if d in border[b2]:
                        border[b2][d] = 0
    return sides


###10:12
file = open('example.txt','r')
# file = open('input.txt','r')

garden = []
plants = {}
seen = []
j = 0
for line in file.readlines():
    tline = []
    for i in range(len(line.strip())):
        tline.append(line[i])
        if line[i] not in plants:
            plants[line[i]] = [1,0]
        else:
            plants[line[i]][0] += 1
    garden.append(tline)
    j += 1
mxx = len(garden[0])-1
mxy = len(garden)-1

regions = []
# regions.append(region(0,0))
for j in range(mxy+1):
    for i in range(mxx+1):
        if (i,j) not in seen:
            regions.append(region(i,j))

respart1 = 0
respart2 = 0
for i in range(len(regions)):
    respart1 += regions[i]['p']*regions[i]['a']
    # respart2 += regions[i]['a']*regions[i]['s']

print(f'{respart1=}')
print(f'{respart2=}')
