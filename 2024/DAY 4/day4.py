def print_puzzle(puzzle,items = []):
    for j in range(len(puzzle)):
        for i in range(len(puzzle[0])):
            if (i,j) in items or len(items)==0:
                print(puzzle[j][i], end ='')
            else:
                print('.', end ='')
        print('')


file = open('example.txt','r')
# file = open('input.txt','r')
puzzle = []
for line in file.readlines():
    puzzle.append(line.upper().strip())

xloc = []
mrel = {1:(0,-1),2:(0,1),3:(-1,0),4:(1,0),5:(-1,-1),6:(1,1),7:(-1,1),8:(1,-1)}
arel = {1:(0,-2),2:(0,2),3:(-2,0),4:(2,0),5:(-2,-2),6:(2,2),7:(-2,2),8:(2,-2)}
srel = {1:(0,-3),2:(0,3),3:(-3,0),4:(3,0),5:(-3,-3),6:(3,3),7:(-3,3),8:(3,-3)}
maxx = len(puzzle[0])
maxy = len(puzzle)
# print_puzzle(puzzle)
for j in range(len(puzzle)):
    for i in range(len(puzzle[0])):
        if puzzle[j][i] == 'X':
            xloc.append((i,j))
toshow = []
toshow.extend(xloc)
# print_puzzle(puzzle,toshow)

toshow = []
count = 0
for xl in xloc:
    for mr in mrel:
        x = xl[0]+mrel[mr][0]
        y = xl[1]+mrel[mr][1]
        if (0 <= x <= maxx-1) and (0 <= y <= maxy -1):
            if puzzle[y][x] == 'M':
                xa = xl[0]+arel[mr][0]
                ya = xl[1]+arel[mr][1]
                if (0 <= xa <= maxx-1) and (0 <= ya <= maxy -1):
                    if puzzle[ya][xa] == 'A':
                        xs = xl[0]+srel[mr][0]
                        ys = xl[1]+srel[mr][1]
                        if (0 <= xs <= maxx-1) and (0 <= ys <= maxy -1):
                            if puzzle[ys][xs] == 'S':
                                count +=1
                                toshow.append(xl)
                                toshow.append((x,y))
                                toshow.append((xa,ya))
                                toshow.append((xs,ys))
print(f'Part1 = {count}')
print_puzzle(puzzle,toshow)
rel = [(-1,-1),(1,-1)]
count2 = 0
aloc = []

for j in range(len(puzzle)):
    for i in range(len(puzzle[0])):
        if puzzle[j][i] == 'A':
            aloc.append((i,j))
toshow2 = []
for al in aloc:
    x = al[0]-1
    y = al[1]-1
    if (0 <= x) and (x+2 <= maxx-1) and (0 <= y) and (y+2 <= maxy -1):
        if puzzle[y][x] == 'M':
            if puzzle[y+2][x+2] == 'S':
                if puzzle[y][x+2] == 'M':
                    if puzzle[y+2][x] == 'S':
                        count2 += 1
                        toshow2.append(al)
                        toshow2.append((x,y))
                        toshow2.append((x+2,y+2))
                        toshow2.append((x+2,y))
                        toshow2.append((x,y+2))
                elif puzzle[y][x+2] == 'S':
                    if puzzle[y+2][x] == 'M':
                        count2 += 1
                        toshow2.append(al)
                        toshow2.append((x,y))
                        toshow2.append((x+2,y+2))
                        toshow2.append((x+2,y))
                        toshow2.append((x,y+2))
        elif puzzle[y][x] == 'S':
            if puzzle[y+2][x+2] == 'M':
                if puzzle[y][x+2] == 'M':
                    if puzzle[y+2][x] == 'S':
                        count2 += 1
                        toshow2.append(al)
                        toshow2.append((x,y))
                        toshow2.append((x+2,y+2))
                        toshow2.append((x+2,y))
                        toshow2.append((x,y+2))
                elif puzzle[y][x+2] == 'S':
                    if puzzle[y+2][x] == 'M':
                        count2 += 1
                        toshow2.append(al)
                        toshow2.append((x,y))
                        toshow2.append((x+2,y+2))
                        toshow2.append((x+2,y))
                        toshow2.append((x,y+2))

print(f'Part2 = {count2}')
print_puzzle(puzzle,toshow2)