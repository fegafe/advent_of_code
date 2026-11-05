import sys
import heapq
from collections import defaultdict as dd
import time

def printmap(mapp, show = {}, scar = 'X',dcar = None):
    for j in range(mxy):
        for i in range(mxx):
            if (i,j) in show:
                print(show[(i,j)],end='')
            else:
                if dcar:
                    print(dcar,end='')
                else:
                    print(mapp[i][j],end='')
        print('')

def dijkstra(start, finish):
    global distances, previous,enodes
    distances = dd(lambda: int(sys.maxsize))    # Distance from start to node
    previous  = dd(lambda: set())               # Previous node in optimal path from source
    enodes    = {}
    nodes     = []                              # Priority queue of all nodes in Graph
    path      = dd(lambda: [])
    distances[start] = 0                        ##SET START TO DISTANCE 0
    heapq.heappush(nodes, [0, start])

    while nodes:
        smallest = heapq.heappop(nodes)[1]                      ## Vertex in nodes with smallest distance in distances
        if (smallest[0],smallest[1]) == (finish[0],finish[1]):  ## If the closest node is our target save it
            enodes[smallest] = distances[smallest]  ##
            # return distances[smallest]

        for neighbor in add_nodes(smallest):              # Look at all the nodes that this vertex is attached to
            alt = distances[smallest] + neighbor['dist']  # Alternative path distance
            if alt < distances[neighbor['node']]:
                distances[neighbor['node']] = alt
                heapq.heappush(nodes, [alt, neighbor['node']])
                previous[neighbor['node']].add(smallest)
                path[smallest[0],smallest[1]]='X'
            elif alt == distances[neighbor['node']]:      ##for part2, add same distances to previuos
                previous[neighbor['node']].add(smallest)

def add_nodes(node):
    global nodes,g
    cx = node[0]
    cy = node[1]
    cd = node[2]
    for d in dr:
        nx = cx+dr[d][0] 
        ny = cy+dr[d][1]
        if  0 <= nx <= mxx and 0 <= ny <= mxy:
            if maze[nx][ny] == '.':
                if d == cd:
                    yield {'dist':1,'node':(nx,ny,d)}
                elif d != rev[cd]:
                    yield {'dist':1000,'node':(cx,cy,d)}
    
sys.setrecursionlimit(1000000)
start_time = time.time()

# file = open('example.txt','r')
file = open('input.txt','r') ##98520 ##609

tmaze = []
j = 0

for line in file.readlines():
    line = line.strip()
    tmaze.append(line)
    for i in range(len(line)):
        if 'S' == line[i]:
            start = [i,j]
        if 'E' == line[i]:
            end = [i,j]
    j += 1

maze = []
for i in range(len(tmaze[0])):
    col = []
    for j in range(len(tmaze)):
        col.append(tmaze[j][i])
    maze.append(col)

mxx = len(maze)
mxy = len(maze[0])

maze[start[0]][start[1]] = '.'
maze[end[0]][end[1]]     = '.'

dr = {'l' : (1,0),'d' : (0,1),'r' : (-1,0),'u' : (0,-1)}
rev = {'l' : 'r','d' : 'u','r' : 'l','u' : 'd'}
sym = {'l' : '>','d' : 'v','r' : '<','u' : '^'}


nstart = (start[0],start[1],'l')
print(dijkstra(nstart,(end[0],end[1],'x')))
stack = set()
enode = min(enodes,key=enodes.get)
print(enode)

stack.add(enode)
gnodes = set(stack)
while stack:
    chk = stack.pop()
    for nip in previous[chk]:
        if nip not in gnodes:
            gnodes.add(nip)
            stack.add(nip)

gnodes2 = set()
for gn in gnodes:
    gnodes2.add((gn[0],gn[1]))
print(len(gnodes2))

print(f'{time.time() - start_time} seconds')
