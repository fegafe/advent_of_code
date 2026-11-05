def print_map(mapp,mark = []):
    for j in range(len(mapp)):
        for i in range(len(mapp[0])):
            if (i,j) in mark:
                print('#',end='')
            else:
                print(mapp[j][i],end='')
        print('')

def abs(a):
    if a<0:
        return -1*a
    return a

# file = open('example.txt','r')
file = open('input.txt','r')

mapp = []
ant = {}
used = []
j=0
for line in file.readlines():
    tline = []
    line = line.strip()
    for i in range(len(line)):
        tline.append(line[i])
        if line[i] != '.':
            if line[i] not in ant:
                ant[line[i]] = []
            ant[line[i]].append((i,j))
            used.append((i,j))
    mapp.append(tline)
    j +=1

maxy = j
maxx = len(mapp[0])

# print_map(mapp)
# print(f'{maxx}:{maxy}')
antinodes = []
antinodes2 = []
ganti = []
##PART 1
for a in ant:
    for x in ant[a]:
        for y in ant[a]:
            if x == y:
                continue
            dx = int(x[0]-y[0])
            dy = int(x[1]-y[1])
            m=1
            nx = x[0] + m*dx
            ny = x[1] + m*dy
            nx2 = y[0] + 2*m*dx
            ny2 = y[1] + 2*m*dy
            if nx == nx2 and ny == ny2 and 0 <= nx < maxx and 0 <= ny < maxy:
                if (nx,ny) not in antinodes:
                    antinodes.append((nx,ny))
                if(nx,ny) not in ganti:
                    ganti.append((nx,ny))
            for m in range(0,maxx):
                nx3 = x[0] + m*dx
                ny3 = x[1] + m*dy
                if 0 <= nx3 < maxx and 0 <= ny3 < maxy:
                    if (nx3,ny3) not in antinodes2:
                        antinodes2.append((nx3,ny3))
                if(nx3,ny3) not in ganti:
                    ganti.append((nx3,ny3))

# print_map(mapp,ganti)
print(f'part1: {len(antinodes)}')
print(f'part2: {len(antinodes2)}')
# print(antinodes)
