from heapq import heappop, heappush
from itertools import count
import networkx as nx

__all__ = ["greedy_path"]

def greedy_path(G, source, target, heuristic = None, weight = 'weight'):
    #add initial checks, like if the source is correct and if the target is present
    instant = count()
    queue = [(0, next(instant), source, None) ]
    visited = {(source, 0): None}
    while queue:
        _, _, element, parent = heappop(queue)

        if element == target:
            #new function, get_path
            path = [element]
            while parent != None:
                path.append(parent)
                parent = visited[parent]
            path.reverse()
            return path
        
        if element in visited:
            continue
        else: 
            visited[element] = parent

        neighbourhood = []
        if element in G:
            neighbourhood = G[element]

        for neighbour in neighbourhood:
            cost_to_neighbour = heuristic(neighbour)
            neighbour_record = ( cost_to_neighbour, next(instant), neighbour, element)
            heappush(queue, neighbour_record)

        
    raise nx.NetworkXNoPath(f"Node {target} is not connected with {source} ")

