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
        cost, _, element, parent = heappop(queue)

        if element == target:
            #new function, get_path
            path = [element]
            parent, cost_from_source = visited[element, cost]
            while cost_from_source != 0:
                path.append(parent)
                parent, cost_from_source = visited[parent, cost_from_source]
            path.append(parent)
            path.reverse()
            return path

        neighbourhood = G[element]

        for neighbour in neighbourhood:
            cost_to_neighbour = cost + G[element][neighbour][weight]
            visited[neighbour, cost_to_neighbour] = element, cost
            neighbour_record = ( cost_to_neighbour, next(instant), neighbour, element)
            heappush(queue, neighbour_record)
    
    raise nx.NetworkXNoPath(f"Node {target} is not connected with {source} ")

