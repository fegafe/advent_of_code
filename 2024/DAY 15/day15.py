def printmap(mapp, show = [], scar = 'X',dcar = None):
    for j in range(mxy):
        for i in range(mxx):
            if (i,j) in show:
                print(scar,end='')
            else:
                if dcar:
                    print(dcar,end='')
                else:
                    print(mapp[i][j],end='')
        print('')


# file = open('example.txt','r')
file = open('input.txt','r')

boxes = []
walls = []
moves = []
j = 0
gmap = True

for line in file.readlines():
    line = line.strip()
    if gmap:
        if j == 0:
            mxx = len(line)
        for i in range(len(line)):
            if '@' == line[i]:
                irpos = [i,j]
            if 'O' == line[i]:
                boxes.append([i,j])
            if '#' == line[i]:
                walls.append((i,j))
        if line == '':
            mxy = j 
            gmap = False
    else:
        moves.extend(line)
    j += 1

# print(mxx)
# print(mxy)
# print(walls)

mapp = []
for i in range(mxx):
    xrow = []
    for j in range(mxy):
        if irpos == [i,j]:
            xrow.append('@')
        elif (i,j) in walls:
            xrow.append('#')
        elif [i,j] in boxes:
            xrow.append('0')
        else:
            xrow.append('.')
    mapp.append(xrow)

rpos = irpos
# printmap(mapp)
# print(moves)

md = {'^':(0,-1),'>':(1,0),'v':(0,1),'<':(-1,0)}

for m in moves:
    mvbox = []
    npos = [rpos[0]+md[m][0],rpos[1]+md[m][1]]
    tpos = npos
    mv = True

    while mapp[tpos[0]][tpos[1]] != '.' :
        if mapp[tpos[0]][tpos[1]] == '#':
            mv = False
            break
        if mapp[tpos[0]][tpos[1]] == '0':
            mvbox.append([tpos[0],tpos[1]])
        tpos = [tpos[0]+md[m][0],tpos[1]+md[m][1]]
    if mv:
        for box in mvbox:
            if mapp[box[0]][box[1]] != '.':
                mapp[box[0]][box[1]] != '.'
            mapp[box[0]+md[m][0]][box[1]+md[m][1]] = '0'
        mapp[rpos[0]][rpos[1]] = '.'
        mapp[npos[0]][npos[1]] = '@'
        rpos = npos

# print(m)
# printmap(mapp)

respart1 = 0
for i in range(mxx):
    for j in range(mxy):
        if mapp[i][j] == '0':
            respart1 += 100*j+i
print(f'{respart1=}')

###PART 2
##remake mapp
mapp = []
for i in range(mxx):
    xrow = []
    for j in range(mxy):
        if irpos == [i,j]:
            xrow.append('@')
        elif (i,j) in walls:
            xrow.append('#')
        elif [i,j] in boxes:
            xrow.append('0')
        else:
            xrow.append('.')
    mapp.append(xrow)

# printmap(mapp)
map2 = []

for i in range(mxx):
    yrow1 = []
    yrow2 = []
    for j in range(mxy):
        if mapp[i][j] == '#':
            yrow1.append('#')
            yrow2.append('#')
        elif mapp[i][j] == '0':
            yrow1.append('[')
            yrow2.append(']')
        elif mapp[i][j] == '@':
            rpos = [2*i,j]
            yrow1.append('@')
            yrow2.append('.')
        else:
            yrow1.append('.')
            yrow2.append('.')
    map2.append(yrow1)
    map2.append(yrow2)

mxx = len(map2)
# printmap(map2)

def vertical_check(x,y,md):
    if  map2[x][y] == '.':
        return True
    elif   map2[x][y] == '[' and (map2[x][y+md[1]] == '#' or map2[x+1][y+md[1]] == '#'):
        return False
    elif map2[x][y] == ']' and (map2[x][y+md[1]] == '#' or map2[x-1][y+md[1]] == '#'):
        return False
    elif map2[x][y] == '[' and map2[x][y+md[1]] == '.' and map2[x+1][y+md[1]] == '.':
        mvbox.append([x,y])
        mvbox.append([x+1,y])
        return True
    elif map2[x][y] == ']' and map2[x][y+md[1]] == '.' and map2[x-1][y+md[1]] == '.':
        mvbox.append([x,y])
        mvbox.append([x-1,y])
        return True
    elif map2[x][y] == '[':
        mvbox.append([x,y])
        mvbox.append([x+1,y])
        return (vertical_check(x,y+md[1],md) and vertical_check(x+1,y+md[1],md))
    elif map2[x][y] == ']':
        mvbox.append([x,y])
        mvbox.append([x-1,y])
        return (vertical_check(x,y+md[1],md) and vertical_check(x-1,y+md[1],md))

# printmap(map2)
c = 0
for m in moves:
    mvbox = []
    npos = [rpos[0]+md[m][0],rpos[1]+md[m][1]]
    tpos = npos
    mv = True
    if map2[tpos[0]][tpos[1]] != '.' and map2[tpos[0]][tpos[1]] != '#':
        if m in ['<','>'] :
            mvbox.append([tpos[0],tpos[1]])
            while map2[tpos[0]][tpos[1]] != '.' :
                if map2[tpos[0]][tpos[1]] == '#':
                    mv = False
                    break
                tpos = [tpos[0]+md[m][0],tpos[1]+md[m][1]]
                mvbox.append([tpos[0],tpos[1]])
        else:
            mv = vertical_check(tpos[0],tpos[1],md[m])
    if mv and map2[tpos[0]][tpos[1]] != '#':
        pp =False
        # if len(mvbox)>0:
            # pp = True
            # printmap(map2)
        for i in range(len(mvbox)):
            box = mvbox[-1]
            if map2[box[0]][box[1]] != '.':
                map2[box[0]+md[m][0]][box[1]+md[m][1]] = map2[box[0]][box[1]]
                map2[box[0]][box[1]] = '.'
            mvbox.remove(box)

        map2[rpos[0]][rpos[1]] = '.'
        map2[npos[0]][npos[1]] = '@'
        rpos = npos
        # if pp:
            # print(f'{c}:{m}',end='')
            # input()
            # printmap(map2)
            # print('')
    # if c > 76 and c < 80:
        # print(mv)
        # print(f'{c}:{m}',end='')
        # input()
     
        # printmap(map2)
    # if not mv:
        # print(f'{c}:{m}',end='')
        # print('')
        # printmap(map2)
        # input()
        
    c += 1

    
respart2 = 0
for i in range(mxx):
    for j in range(mxy):
        if map2[i][j] == '[':
            respart2 += 100*j+i
print(f'{respart2=}')