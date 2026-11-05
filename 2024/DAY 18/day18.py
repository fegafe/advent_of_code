import sys
import heapq

class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
    
    def shortest_path(self, start, finish):
        distances = {} # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = [] # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start: # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None
        
        while nodes:
            smallest = heapq.heappop(nodes)[1] # Vertex in nodes with smallest distance in distances
            if smallest == finish: # If the closest node is our target we're done so print the path
                path = []
                while previous[smallest]: # Traverse through nodes til we reach the root which is 0
                    path.append(smallest)
                    smallest = previous[smallest]
                return path
            if distances[smallest] == sys.maxsize: # All remaining vertices are inaccessible from source
                break
            
            for neighbor in self.vertices[smallest]: # Look at all the nodes that this vertex is attached to
                alt = distances[smallest] + self.vertices[smallest][neighbor] # Alternative path distance
                if alt < distances[neighbor]: # If there is a new shortest path update our priority queue (relax)
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances
        
    def __str__(self):
        return str(self.vertices)

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

def solvemaze(pos,rc,cd,seen):
    global minrc
    if rc >= minrc:
        return False,rc
    seenl = []
    seenl.extend(seen)
    seenl.append(((pos[0],pos[1]),cd))
    if not (0<= pos[0] <= gs and 0<= pos[1] <= gs):
        return False,0
    elif pos == end:
        return True,rc
    elif maze[pos[0]][pos[1]] == '#':
        return False,0
    elif maze[pos[0]][pos[1]] == '.':
        routes = []
        for d in dr:
            if  0 <= pos[0]+dr[d][0] <= gs and 0 <= pos[1]+dr[d][1] <= gs:
                if maze[pos[0]+dr[d][0]][pos[1]+dr[d][1]] in ['.'] and d != rev[cd] and ((pos[0]+dr[d][0],pos[1]+dr[d][1]),d) not in seenl and ((pos[0]+dr[d][0],pos[1]+dr[d][1]),rev[cd]) not in seenl:
                    if d != cd:
                        chk,trc = solvemaze([pos[0]+dr[d][0],pos[1]+dr[d][1]],rc+1,d,seenl)
                    else:
                        chk,trc = solvemaze([pos[0]+dr[d][0],pos[1]+dr[d][1]],rc+1,d,seenl)
                    if chk:
                        routes.append(trc)
        if len(routes)>0:
            if min(routes) < minrc:
                minrc = min(routes)
            return True,min(routes)
        else:
            return False,0

def add_nodes(pos):
    global nodes,g
    edges = {}
    for d in dr:
        if  0 <= pos[0]+dr[d][0] <= gs and 0 <= pos[1]+dr[d][1] <= gs:
            if maze[pos[0]+dr[d][0]][pos[1]+dr[d][1]] == '.':
                edges[f'{pos[0]+dr[d][0]}.{pos[1]+dr[d][1]}'] = 1
                nodes.add((pos[0]+dr[d][0],pos[1]+dr[d][1]))
    g.add_vertex(f'{pos[0]}.{pos[1]}',edges)

def dijkstra():
    global nodes,g
    g = Graph()
    nodes = set()
    nodes.add((0,0))
    while len(nodes) > 0:
        nn = nodes.pop()
        if f'{nn[0]}.{nn[1]}' not in g.vertices:
            add_nodes([nn[0],nn[1]])
    # print(g.vertices)
    return g.shortest_path('0.0', f'{gs}.{gs}')

# file = open('example.txt','r')
# gs = 6
# nb = 12
file = open('input.txt','r')
gs = 70
nb = 1024
sys.setrecursionlimit(1000000)

grid = []
obs = []
for line in file.readlines():
    line = line.strip()
    x,y = line.split(',')
    obs.append((int(x),int(y)))
# print(obs)

mxx = gs+1
mxy = gs+1
for i in range(mxx):
    tcol = []
    for j in range(mxy):
        tcol.append('.')
    grid.append(tcol)

# printmap(grid,obs[:nb],'#')
# print('')
maze = []
for i in range(mxx):
    tcol = []
    for j in range(mxy):
        if (i,j) in obs[:nb]:
            tcol.append('#')
        else:
            tcol.append('.')
    maze.append(tcol)
# printmap(maze)

dr = {'l' : (1,0),'d' : (0,1),'r' : (-1,0),'u' : (0,-1)}

respart1 = dijkstra()
# print(respart1)
print(len(respart1))
# print(obs[nb:])
# print(obs[:nb])
for nby in obs[nb:]:
    maze[nby[0]][nby[1]] = '#'
    if f'{nby[0]}.{nby[1]}' in respart1:
        # print(nby)
        # printmap(maze)
        respart1 = dijkstra()
        # print(respart1)
        if isinstance(respart1, dict):
            print(f'respart2 = {nby}')
            break
