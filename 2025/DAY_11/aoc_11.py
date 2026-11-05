import time
import sys
import heapq
import collections
from collections import defaultdict

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
        previous  = {} # Previous node in optimal path from source
        nodes     = [] # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start: # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None
        
        while nodes:
            smallest = heapq.heappop(nodes)[1]       # Vertex in nodes with smallest distance in distances
            if smallest == finish:                   # If the closest node is our target we're done so print the path
                path = []                            
                while previous[smallest]:            # Traverse through nodes til we reach the root which is 0
                    path.append(smallest)            
                    smallest = previous[smallest]    
                return path,distances                
            if distances[smallest] == sys.maxsize:   # All remaining vertices are inaccessible from source
                break
            
            for neighbor in self.vertices[smallest]: # Look at all the nodes that this vertex is attached to
                alt = distances[smallest] + self.vertices[smallest][neighbor] # Alternative path distance
                if alt < distances[neighbor]:        # If there is a new shortest path update our priority queue (relax)
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances

    def allPaths(self, s, d, f = None):
        # Mark all the vertices as not visited
        visited       = {}
        self.dfspaths = []
        self.cache    = {}
        for v in self.vertices:
            visited[v] = False
        if f:
            visited[f] = True
        # Create an array to store paths
        path = []
        # Call the recursive helper function to print all paths
        self.allPathsUtil(s, d, visited, path)
        return self.dfspaths

    def count(self,s,d):
        # Mark all the vertices as not visited
        visited       = {}
        self.dfspaths = []
        self.cache    = {}
        for v in self.vertices:
            visited[v] = False
        path = []
        return self.count_paths(s,d,visited,path)

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

    def count_paths(self, u, d, visited, path):
        global p2
        visited[u]= True 
        path.append(u)
        if (u,d) in self.cache:
            return self.cache[(u,d)]
        r = 0
        if u == d:
            p = path.copy()
            self.dfspaths.append(p)
            r = 1
        else:
            for i in self.vertices[u]:
                # if visited[i] == False: ##COMENT FOR ALL PATHS
                r += self.count_paths(i, d, visited, path)
            self.cache[(u,d)] = r
        path.pop()
        visited[u]= False 
        return r

    def __str__(self):
        return str(self.vertices)

start_time = time.perf_counter()

sys.setrecursionlimit(1000000)
##some = defaultdict(int)

# file = open('example.txt','r')
# file = open('example_2.txt','r')
file = open('input.txt','r')
p1 = 0
p2 = 1

g = Graph()
for sline in file.readlines():
    line = sline.strip().split(':')
    g.add_vertex(line[0],line[1].strip().split())

g.add_vertex('out',[])
val = []
val.append(g.count('dac','out'))
val.append(g.count('dac','fft'))### this is 0 so 
val.append(g.count('fft','dac'))
val.append(g.count('svr','fft'))


for l in range(len(val)):
    if val[l] > 0:
        p2 *= val[l]
print(f'Part2: {p2}')

print(f"Execution time: {(time.perf_counter() - start_time):.4f} seconds")

##TOLOW
# 23572684800
# 23331587328
# 73423542528
# 377452269415704