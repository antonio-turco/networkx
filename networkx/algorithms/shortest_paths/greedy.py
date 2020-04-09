from heapq import heappop, heappush
from itertools import count
import networkx as nx

__all__ = ["greedy_path"]

def greedy_path(G, source, target, heuristic = None, weight = 'weight'):
    if heuristic != None:
        h = lambda node: heuristic(node, target)
    else:
        h = lambda node: 1        

    instant = count()
    queue = [(0, next(instant), source, None) ]
    visited = {(source, 0): None}
    while queue:
        _, _, element, parent = heappop(queue)

        if element == target:
            return get_path(element, parent, visited)
        
        if not element in visited:
            visited[element] = parent
            neighbourhood = get_neighbourhood(G, element)
            push_neighbourhood(queue, neighbourhood, element, h, instant)

        
    raise nx.NetworkXNoPath(f"Node {target} is not connected with {source} ")

def get_path( element, parent, visited ):
    path = [element]
    while parent != None:
        path.append(parent)
        parent = visited[parent]
    path.reverse()
    return path

def get_neighbourhood(g, element):
    neighbourhood = []
    if element in g:
        neighbourhood = g[element]
    return neighbourhood

def push_neighbourhood(queue, neighbourhood, parent, h, instant):
    for neighbour in neighbourhood:
        cost_to_neighbour = h(neighbour)
        neighbour_record = ( cost_to_neighbour, next(instant), neighbour, parent)
        heappush(queue, neighbour_record)