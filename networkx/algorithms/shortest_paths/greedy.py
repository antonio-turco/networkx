from heapq import heappop, heappush
from itertools import count
import networkx as nx

__all__ = ["greedy_path"]

def greedy_path(G, source, target, heuristic = None, weight = 'weight'):
    print("greedy hello!")

    '''
    
    create queue with source
    while not empty queue
        take first
        if is target --> stop
        else 
            take the neighbourhood
            take the dist and sum it to the actual cost
            place them in the queue

    '''

    instant = count()
    queue = [(0, next(instant), source, None) ]
    visited = {}
    while queue:
        cost, _, element, parent = heappop(queue)
        if element == target:
            #must return path, so you need to scan all the parents chain
            return element, parent
        neighbourhood = G[element]
        for neighbour in neighbourhood:
            if not neighbour in visited:
                neighbour_record = (cost + G[element][neighbour][weight], next(instant), neighbour, element)
                heappush(queue, neighbour_record)
