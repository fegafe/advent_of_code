
def trail(x,init):
    respart1 = 0
    # print(f'{x}:{map_[x[1]][x[0]]}')
    if (map_[x[1]][x[0]]) == 9:
        if init in end[x]:
            return 1
            ##return 0##part 1
        end[x].append(init)
        return 1
    nx = x[0]+1
    if 0<=nx<=maxx:
        if map_[x[1]][nx] == map_[x[1]][x[0]]+1:
            respart1 += trail((nx,x[1]),init)
    nx = x[0]-1
    if 0<=nx<=maxx:
        if map_[x[1]][nx] == map_[x[1]][x[0]]+1:
            respart1 += trail((nx,x[1]),init)
    ny = x[1]+1
    if 0<=ny<=maxy:
        if map_[ny][x[0]] == map_[x[1]][x[0]]+1:
            respart1 += trail((x[0],ny),init)
    ny = x[1]-1
    if 0<=ny<=maxy:
        if map_[ny][x[0]] == map_[x[1]][x[0]]+1:
            respart1 += trail((x[0],ny),init)
    return respart1

# file = open('example.txt','r')
file = open('input.txt','r')

map_ = []
start = {}
end = {}
j=0
for line in file.readlines():
    tline = []
    for i in range(len(line.strip())):
        tline.append(int(line[i]))
        if int(line[i]) == 0:
            start[(i,j)] = 0
        elif int(line[i]) == 9:
            end[(i,j)] = []
    map_.append(tline)
    j += 1

# print(start)
# print(end)

# for j in range(len(map_)):
    # for i in range(len(map_[0])):
        # print(map_[j][i],end='')
    # print('')
    
maxy = len(map_)-1
maxx = len(map_[0])-1
# print(f'{maxx}:{maxy}')

# print(trail((2,0),(2,0)))
res1 = 0
for x in start:
    res1 += trail(x,x)
print(f'{res1=}')
