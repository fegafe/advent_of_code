import sys
import heapq
import collections
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
                return path,distances
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

def add_nodes(pos):
    global nodes,g
    edges = {}
    for d in dr:
        if  0 <= pos[0]+dr[d][0] <= mxx and 0 <= pos[1]+dr[d][1] <= mxy:
            if maze[pos[0]+dr[d][0]][pos[1]+dr[d][1]] != '#':
                edges[(pos[0]+dr[d][0],pos[1]+dr[d][1])] = 1
                nodes.add((pos[0]+dr[d][0],pos[1]+dr[d][1]))
    g.add_vertex((pos[0],pos[1]),edges)

def dijkstra():
    global nodes,g
    seen = []
    g = Graph()
    nodes = set()
    nodes.add(start)
    nodes.add(end)
    while len(nodes) > 0:
        nn = nodes.pop()
        if nn not in seen:
            add_nodes(nn)
        seen.append(nn)
    return g.shortest_path(end, start)

# file = open('example.txt','r')
file = open('input.txt','r')

sys.setrecursionlimit(1000000)

tmaze = []
j = 0
for line in file.readlines():
    line = line.strip()
    tmaze.append(line)
    for i in range(len(line)):
        if 'S' == line[i]:
            start = (i,j)
        if 'E' == line[i]:
            end = (i,j)
    j += 1
maze = []
for i in range(len(tmaze[0])):
    col = []
    for j in range(len(tmaze)):
        col.append(tmaze[j][i])
    maze.append(col)
dr = {'l' : (1,0),'d' : (0,1),'r' : (-1,0),'u' : (0,-1)}

mxx = len(maze)
mxy = len(maze[0])

path,dist = dijkstra()

i = 0
res = {}
path.append(end)
respart1 = 0
respart2 = 0
for x in path:
    for x2 in path[i+1:]:
        if (abs(x[0]-x2[0])+abs(x[1]-x2[1])) == 2:
            saved = dist[x]-dist[x2] -2
            if saved >= 100:
                respart1 += 1
        if 2 <= (abs(x[0]-x2[0])+abs(x[1]-x2[1])) <= 20:
            saved = dist[x] - (dist[x2] + (abs(x[0]-x2[0])+abs(x[1]-x2[1])))
            if saved >= 100:
                respart2 += 1
                # if saved not in res:
                    # res[saved] = []
                # res[saved].append((x,x2))
    i += 1

print(f'{respart1=}')
print(f'{respart2=}')

