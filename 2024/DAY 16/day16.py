import sys
import heapq
import time


class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, edges):
        if name in self.vertices:
            for e in edges:
                self.vertices[name][e] = edges[e]
        else:
            self.vertices[name] = edges
    
    def shortest_path(self, start, finish):
        distances = {} # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = [] # Priority queue of all nodes in Graph
        path = []
        lowercost = sys.maxsize
        for vertex in self.vertices:
            if vertex == start: # Set root node as distance of 0
                distances[vertex] = 0                       ##SET START TO DISTANCE 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize             ##SET ALL DISTANCES TO MAXSIZE
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None
        while nodes:
            smallest = heapq.heappop(nodes)[1]          ## Vertex in nodes with smallest distance in distances
            ##comented for part2 FIND EVERY DISTANCES
            if smallest == finish:                      ## If the closest node is our target we're done so print the path
                lowercost = min(lowercost,distances[finish])
                while previous[smallest]:               ## Traverse through nodes til we reach the root which is 0
                    path.append(smallest)
                    smallest = previous[smallest]
                path.append(start)
                return lowercost,path
            
            if distances[smallest] == sys.maxsize:      ## All remaining vertices are inaccessible from source
                print("All remaining vertices are inaccessible from source")
                break
            
            for neighbor in self.vertices[smallest]:    # Look at all the nodes that this vertex is attached to
                alt = distances[smallest] + self.vertices[smallest][neighbor] # Alternative path distance
                if neighbor in distances:
                    if alt < distances[neighbor]:           ##If there is a new shortest path update our priority queue (relax)
                        distances[neighbor] = alt
                        previous[neighbor]  = smallest      ##Set previous node if distance 
                        for n in nodes:                     ##UPDATE ALL distances 
                            if n[1] == neighbor:
                                n[0] = alt
                                break
                        heapq.heapify(nodes)          ##reorder heap to small to pop
        return sys.maxsize,distances
        
    def __str__(self):
        return str(self.vertices)

    def allPathsUtil(self, u, d, visited, path):
        # Mark the current node as visited and store in path
        visited[u]= True
        path.append(u)
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            self.dfspaths.append(path.copy())
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.vertices[u]:
                if i in visited:
                    if visited[i]== False:
                        self.allPathsUtil(i, d, visited, path)
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False

    # Prints all paths from 's' to 'd'
    def allPaths(self, s, d):
        # Mark all the vertices as not visited
        visited = {}
        self.dfspaths = []
        for v in self.vertices:
            visited[v] = False
        # Create an array to store paths
        path = []
        # Call the recursive helper function to print all paths
        self.allPathsUtil(s, d, visited, path)
        return self.dfspaths
    
    def allpathsminlen(self, s, d):
        mpaths = []
        self.allPaths(s, d)
        minlen = sys.maxsize
        lengths = {}
        for p in range(len(self.dfspaths)):
            if len(self.dfspaths[p])<minlen:
                minlen = len(self.dfspaths[p])
        for p in range(len(self.dfspaths)):
            if len(self.dfspaths[p]) == minlen:
                mpaths.append(self.dfspaths[p])
        return mpaths


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

def add_nodes(pos):
    global nodes,g
    cx = pos[0]
    cy = pos[1]
    cd = pos[2]
    for d in dr:
        nx = cx+dr[d][0] 
        ny = cy+dr[d][1]
        if  0 <= nx <= mxx and 0 <= ny <= mxy:
            if maze[nx][ny] == '.':
                if d == cd:
                    g.add_vertex(pos,{(nx,ny,d):1})
                    nodes.add((nx,ny,d))
                elif d != rev[cd]:
                    g.add_vertex(pos,{(cx,cy,d):1000})
                    nodes.add((cx,cy,d))
    
def dijkstra(start,end):
    global nodes,g
    seen = []
    g = Graph()
    nodes = set()
    nodes.add(start)
    nodes.add(end)
    g.add_vertex(start,{})
    g.add_vertex(end,{})
    while nodes:
        nn = nodes.pop()
        if nn not in seen:
            add_nodes(nn)
            seen.append(nn)
    print('done adding nodes')
    # cost,path,dis = g.shortest_path(start, end)
    return g.shortest_path(start, end)

sys.setrecursionlimit(1000000)
# file = open('example.txt','r')
file = open('input.txt','r') ##98520 
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


dr = {'l' : (1,0),'d' : (0,1),'r' : (-1,0),'u' : (0,-1)}
rev = {'l' : 'r','d' : 'u','r' : 'l','u' : 'd'}
sym = {'l' : '>','d' : 'v','r' : '<','u' : '^'}
mxx = len(maze)
mxy = len(maze[0])

# print(start)
# print(end)

maze[start[0]][start[1]] = '.'
maze[end[0]][end[1]]     = '.'

start_time = time.time()
cost,pathr = dijkstra((start[0],start[1],'l'),(end[0],end[1],'l'))
print(f'respart1 = {cost}')

print(f'{time.time() - start_time} seconds')

# gpaths = g.allpathsminlen((start[0],start[1],'l'),(end[0],end[1],'l'))
# part2 = set()

# for gp in gpaths:
    # for n in gp:
        # part2.add((n[0],n[1]))

# show ={}

# for n in part2:
    # show[n] = '0'
# printmap(maze,show)
# print(f'respart2 = {len(part2)}')
