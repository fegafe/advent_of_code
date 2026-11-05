import time
import sys
import heapq
import collections
from collections import defaultdict

sys.setrecursionlimit(1000000)

def dijkstra_infinite(start_node, target_node, get_neighbors_func,buttons):
    # Use a dictionary to store distances of visited/queued nodes
    distances = {start_node: 0}
    # Priority queue stores (distance, node)
    priority_queue = [(0, start_node)]
    visited = set()
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        # Skip if already fully processed (due to Python's heapq limitations with updates)
        if current_node in visited:
            continue
        visited.add(current_node)
        # Termination condition: found the target
        if current_node == target_node:
            return current_distance
        # Dynamically generate and process neighbors
        for neighbor, weight in get_neighbors_func(current_node,buttons,target_node).items():
            path_distance = current_distance + weight
            # If a shorter path to the neighbor is found, update its distance and queue it
            if path_distance < distances.get(neighbor, sys.float_info.max):
                distances[neighbor] = path_distance
                heapq.heappush(priority_queue, (path_distance, neighbor))
    return sys.float_info.max # Target not reachable

# Define a function to get neighbors in a 2D infinite grid
def get_grid_neighbors(node,buttons,target):
    neighbors = {}
    cval = list(node)
    for b in buttons:
        nnode= tuple([a ^ b for a, b in zip(cval, b)])
        neighbors[nnode] = 1
    # print(f'{node}->{neighbors}')
    return neighbors

def get_grid_neighbors2(node,buttons,target):
    neighbors = {}
    cval = list(node)
    for b in buttons:
        nnode = [a + b for a, b in zip(cval, list(b))]
        check = [a - b for a, b in zip(list(target), nnode)]
        if min(check) >= 0:
            neighbors[tuple(nnode)] = 1
    return neighbors

start_time = time.perf_counter()

file = open('example.txt','r')
file = open('input.txt','r')
p1   = 0
p2   = 0
swi  = []
buts = []
jolt = []
for sline in file.readlines():
    line = sline.strip().split()
    swi.append(line[0])
    buts.append(line[1:-1])
    jolt.append(line[-1])

lights = []
for s in swi:
    tval = []
    for i,c in enumerate(s[1:-1]):
        if c == '#':
            tval.append(1)
        else:
            tval.append(0)
    lights.append(tuple(tval))

buttons = []
for i,but in enumerate(buts):
    cbuttons = []
    size = len(lights[i])
    for b in but:
        vals = [int(x) for x in b[1:-1].split(',')]
        cbut = [0]*size
        for i in range(size):
            if i in vals:
                cbut[i] = 1
        cbuttons.append(tuple(cbut))
    buttons.append(cbuttons)

for i,l in enumerate(lights):
    start = tuple([0]*len(l))
    target = l
    shortest_dist = dijkstra_infinite(start, target, get_grid_neighbors,buttons[i])
    # print(f"Shortest distance from {start} to {target}: {shortest_dist}")
    p1 += shortest_dist

print(f'Part1: {p1}')
print(f"Execution time P1: {(time.perf_counter() - start_time):.4f} seconds")

j = jolt[0]
vtarget = ([int(x) for x in j[1:-1].split(',')])
target  = tuple(vtarget)
start   = tuple([0]*len(target))
print(f"from {start} to {target}")
shortest_dist = dijkstra_infinite(start, target, get_grid_neighbors2,buttons[0])
print(f"Shortest distance from {start} to {target}: {shortest_dist}")

# for i,j in enumerate(jolt):
    # vtarget = ([int(x) for x in j[1:-1].split(',')])
    # target  = tuple(vtarget)
    # start = tuple([0]*len(target))
    # nnode   = start
    # ntarget = target
    # cd = 0
    # while nnode != target:
        # mint = sys.maxsize
        # pb = []
        # for k in range(len(ntarget)):
            # if ntarget[k] > 0:
                # pb.append(1)
                # if ntarget[k] < mint:
                    # mint = ntarget[k]
            # else:
                # pb.append(0)
        # dist = mint*dijkstra_infinite(start, tuple(pb), get_grid_neighbors,buttons[i])
        # nnode   = tuple([a + b*mint for a, b in zip(list(nnode), pb)])
        # ntarget = tuple([a - b*mint for a, b in zip(ntarget, pb)])
        # # print(f'nnode {nnode}: {dist} {pb} {ntarget}')
        # cd += dist
    # print(f'{start} to {target} took {cd}')
    # p2 += cd
    # for b in buttons2[i]:
        # print(b)
    # target = l
    # shortest_dist = dijkstra_infinite(start, target, get_grid_neighbors2,buttons2[i])
    # print(f"Shortest distance from {start} to {target}: {shortest_dist}")
    # p2 += shortest_dist 
    # print(f'{i}/{len(jolt)} {(time.perf_counter() - start_time):.4f} seconds')

print(f'Part2: {p2}')
print(f"Execution time: {(time.perf_counter() - start_time):.4f} seconds")
