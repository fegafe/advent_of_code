
def print_map(mapc,inp = []):
    wid = len(mapc[0])
    hei = len(mapc)
    path = []
    for x in inp:
        path.append((x[0],x[1]))
    for j in range(hei):
        for i in range(wid):
            if (i,j) in path:
                print('X',end='')
            else:
                print(mapc[j][i],end='')
        print('')

def pathbuild(mapc,init):
    out = False
    loop = False
    path = []
    path.append(init)
    wid = len(mapc[0])
    hei = len(mapc)
    while not out:
        x, y, direc = path[-1]
        ny,nx = y,x
        if direc =='u':
            ndir = 'r'
            ny = y-1
        elif direc == 'd':
            ndir = 'l'
            ny = y+1
        elif direc == 'l':
            ndir = 'u'
            nx = x-1
        elif direc == 'r':
            ndir = 'd'
            nx = x+1
        if ny < 0 or nx < 0 or ny >= hei or nx >= wid:
            out = True
        elif mapc[ny][nx] == '#':
            path[-1] = (path[-1][0],path[-1][1],ndir)
        else:
            path.append((nx,ny,direc))
    return path

def is_loop(mapc,init):
    out = False
    loop = False
    path = []
    path.append(init)
    wid = len(mapc[0])
    hei = len(mapc)
    while not out:
        x, y, direc = path[-1]
        ny,nx = y,x
        if direc =='u':
            ndir = 'r'
            ny = y-1
        elif direc == 'd':
            ndir = 'l'
            ny = y+1
        elif direc == 'l':
            ndir = 'u'
            nx = x-1
        elif direc == 'r':
            ndir = 'd'
            nx = x+1
        if ny < 0 or nx < 0 or ny >= hei or nx >= wid:
            out = True
            loop = False
        elif mapc[ny][nx] == '#':
            if(x,y,ndir) in path:
                out = True
                loop = True
            else:
                path[-1] = (x,y,ndir)
        else:
            if(nx,ny,direc) in path:
                out = True
                loop = True
            else:
                path.append((nx,ny,direc))
    return loop

# file = open('example.txt','r')
file = open('input.txt','r')

mapp = []
j = 0

for line in file.readlines():
    mapp.append(line)
    if '^' in line:
        for i in range(len(line)):
            if line[i] == '^':
                init = (i,j,'u')
    j += 1

wid = len(mapp[0])-1
hei = len(mapp)

mapor = []
for j in range(hei):
    tline = []
    for i in range(wid):
        tline.append(mapp[j][i])
    mapor.append(tline)

pathor = pathbuild(mapor,init)
respart1 = 0
respart2 = 0

uni = []
checked = []
c = 0

# print(len(mapor))
# print(len(mapor[0]))

for x in pathor:
    if (x[0],x[1]) not in uni:
        uni.append((x[0],x[1]))
        respart1 += 1
        if c > 0 and x != init and mapor[x[1]][x[0]] == '.':
            mapor[x[1]][x[0]] = '#'
            if is_loop(mapor,init):
                respart2 += 1
            mapor[x[1]][x[0]] = '.'
    c += 1
    if c%100 == 0:
        print(f'{c=} of {len(pathor)}')
print(f'{respart1=}')
print(f'{respart2=}')
