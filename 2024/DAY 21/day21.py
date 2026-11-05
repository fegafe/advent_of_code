import sys
import heapq
import collections
class Graph:
    
    def __init__(self):
        self.vertices = {}
        self.dfspaths = []
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
                return path,distances[start]
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
        '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
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

def get_npath3(s,d,pk1='A'):
    apaths = gkp.allpathsminlen(s,d)
    res = []
    for apath in apaths:
        npath=[]
        
        # print(path)
        for l in range(len(apath)-1):
            npath.append(dr[(kp[apath[l+1]][0] - kp[apath[l]][0] , kp[apath[l+1]][1] - kp[apath[l]][1])])
        npath.append('A')
        # print(npath)
        ##2nd robot
        npath2 = []
        
        cpk2 = pk1
        for pk in npath:
            path = []
            path = gkp2.shortest_path(cpk2, pk)[0]
            path.append(cpk2)
            path = list(reversed(path))
            for l in range(len(path)-1):
                npath2.append(dr[(kp2[path[l+1]][0] - kp2[path[l]][0] , kp2[path[l+1]][1] - kp2[path[l]][1])])
            npath2.append('A')
            cpk2 = pk

        # print(npath2)
        npath3 = []
        cpk = pk2
        for pk in npath2:
            path = []
            path = gkp2.shortest_path(cpk, pk)[0]
            path.append(cpk)
            path = list(reversed(path))
            for l in range(len(path)-1):
                npath3.append(dr[(kp2[path[l+1]][0] - kp2[path[l]][0] , kp2[path[l+1]][1] - kp2[path[l]][1])])
            npath3.append('A')
        # print(npath3)
        res.append(npath3)
        print(f'{apath}:{npath3}:{len(npath3)}')
    # for x in res:
        # print(f'{x}::{len(x)}')
    return res,cpk2
# # +---+---+---+
# # | 7 | 8 | 9 |
# # +---+---+---+
# # | 4 | 5 | 6 |
# # +---+---+---+
# # | 1 | 2 | 3 |
# # +---+---+---+
    # # | 0 | A |
    # # +---+---+

    # # +---+---+
    # # | ^ | A |
# # +---+---+---+
# # | < | v | > |
# # +---+---+---+

kp  = {'0':(1,3),'A':(2,3),'1':(0,2),'2':(1,2),'3':(2,2),'4':(0,1),'5':(1,1),'6':(2,1),'7':(0,0),'8':(1,0),'9':(2,0)}
kp2 = {'<':(0,1),'v':(1,1),'>':(2,1),'^':(1,0),'A':(2,0)}

dr = {(1,0):'>',(0,-1):'^',(0,1):'v',(-1,0):'<'}
drc = {(1,0):1,(0,-1):1,(0,1):1,(-1,0):2}
gkp = Graph()
gkp2 = Graph()
gkp3 = Graph()

for k in kp2:
    for d in dr:
        for k2 in kp2:
            if kp2[k][0]+d[0] == kp2[k2][0] and kp2[k][1]+d[1] == kp2[k2][1]:
                gkp2.add_vertex(k,{k2:drc[d]})

for k in kp:
    for d in dr:
        for k2 in kp:
            if kp[k][0]+d[0] == kp[k2][0] and kp[k][1]+d[1] == kp[k2][1]:
                gkp.add_vertex(k,{k2:1})


pk0 = 'A'
pk1 = 'A'
pk2 = 'A'
pk3 = 'A'

exa = """029A
980A
179A
456A
379A"""

inp = """140A
180A
176A
805A
638A"""

# inp = exa

sys.setrecursionlimit(1000000)
respart1 = 0
codes = []
for line in inp.split('\n'):
    line = line.strip()
    codes.append(line)

res = {}
cache = {}

for cod in codes:
    res[cod] = {}
    ###for all codes
    allpaths = {}
    i = 0
    cpk = 'A'

    for pk in cod:
        allpaths[i] = gkp.allpathsminlen(cpk,pk)
        cpk=pk
        i += 1
    apaths = []
    for p1 in allpaths[0]:
        for p2 in allpaths[1]:
            for p3 in allpaths[2]:
                for p4 in allpaths[3]:
                    apaths.append([p1,p2,p3,p4])

    for apath in apaths:
        npath = []
        cpk = pk0
        for path in apath:
            for l in range(len(path)-1):
                npath.append(dr[(kp[path[l+1]][0] - kp[path[l]][0] , kp[path[l+1]][1] - kp[path[l]][1])])
            npath.append('A')
        print(f'{cod}::::{len(path)}::{"".join(npath)}')
        ##2nd robot
        npath2 = []
        npath2.append(npath)
        r = 0
        i = 0
        while r < 2:
            tnpath2 = []
            cpk = pk1
            for pk in npath2[-1]:
                if (cpk,pk) not in cache:
                    path = []
                    path = gkp2.shortest_path(cpk, pk)[0]
                    path.append(cpk)
                    path = list(reversed(path))
                    tap = []
                    for l in range(len(path)-1):
                        tap.append(dr[(kp2[path[l+1]][0] - kp2[path[l]][0] , kp2[path[l+1]][1] - kp2[path[l]][1])])
                        tnpath2.append(dr[(kp2[path[l+1]][0] - kp2[path[l]][0] , kp2[path[l+1]][1] - kp2[path[l]][1])])
                    cache[(cpk,pk)] = tap.copy()
                else:
                    tap = cache[(cpk,pk)].copy()
                    tnpath2.extend(tap.copy())
                tnpath2.append('A')
                cpk = pk
            npath2.append(tnpath2.copy())
            i += 1
            print(f'{cod}::{r:2}::{len(npath2[-1])}::{"".join(npath2[-1])}')
            r += 1
        res[cod][len(npath2[-1])] = npath2[-1].copy()
        # print(cache)
        

respart2 = 0
minpaths = {}
for cod in codes:
    codnum = []
    for d in cod:
        if d.isdigit():
            codnum.append(d)
    cnum = int(''.join(codnum))
    mink = sys.maxsize
    for k in res[cod]:
        if k<mink:
            mink = k
    minpaths[cod] = {}
    minpaths[cod]['size'] = mink
    minpaths[cod]['path'] = res[cod][mink]
    minpaths[cod]['cnum'] = cnum
    respart1 +=len(res[cod][mink])*cnum
    # print(f'{cod}::{cnum}*{len(res[cod][mink])}={len(res[cod][mink])*cnum}:{"".join(res[cod][mink])}')

print(f'{respart1 = }')
cache2 = {}

# posval = ['<','>','v','^','A']
# valpath = {}
# for val in posval:
    # lnpath = val
    # r = 0
    # while r < 15:
        # tnpath2 = []
        # cpk = pk1
        # ca = 0
        # for pk in lnpath:
            # if (cpk,pk) not in cache:
                # path = []
                # path = gkp2.shortest_path(cpk, pk)[0]
                # path.append(cpk)
                # path = list(reversed(path))
                # tap = []
                # for l in range(len(path)-1):
                    # tap.append(dr[(kp2[path[l+1]][0] - kp2[path[l]][0] , kp2[path[l+1]][1] - kp2[path[l]][1])])
                    # tnpath2.append(dr[(kp2[path[l+1]][0] - kp2[path[l]][0] , kp2[path[l+1]][1] - kp2[path[l]][1])])
                # cache[(cpk,pk)] = tap.copy()
            # else:
                # tnpath2.extend(cache[(cpk,pk)])
            # tnpath2.append('A')
            # cpk = pk
        # lnpath = tnpath2
        # # print(''.join(lnpath))
        # r += 1
    # print(f'{val}::{r:02}::{len(lnpath)}')
    # valpath[val] = len(lnpath)

# respart2 = 0

# for cod in minpaths:
    # npath = minpaths[cod]['path']
    # lnpath = npath.copy()
    # r = 0
    # shp = []
    # while r < 8:
        # tnpath2 = []
        # cpk = pk1
        # ca = 0
        # for pk in lnpath:
            # if (cpk,pk) not in cache:
                # path = []
                # path = gkp2.shortest_path(cpk, pk)[0]
                # path.append(cpk)
                # path = list(reversed(path))
                # tap = []
                # for l in range(len(path)-1):
                    # tap.append(dr[(kp2[path[l+1]][0] - kp2[path[l]][0] , kp2[path[l+1]][1] - kp2[path[l]][1])])
                    # tnpath2.append(dr[(kp2[path[l+1]][0] - kp2[path[l]][0] , kp2[path[l+1]][1] - kp2[path[l]][1])])
                # cache[(cpk,pk)] = tap.copy()
            # else:
                # tnpath2.extend(cache[(cpk,pk)])
            # tnpath2.append('A')
            # cpk = pk
        # lnpath = tnpath2
        # # print(f'{cod}::{r:2}::{len(lnpath)}')
        # r += 1
    # tlen = 0
    # for pk in lnpath:
        # tlen += valpath[pk]
    # minpaths[cod]['part2'] = tlen
    # print(f'{cod}::{tlen}')
    # respart2 += minpaths[cod]['part2']*minpaths[cod]['cnum']

# print(f'{respart2 = }') ##Too low   13290628588600
                        # ##Too high 267183096129706
                        # ##Too high 686192175850845