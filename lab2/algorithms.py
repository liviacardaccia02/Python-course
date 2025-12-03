from basicgraph import adjacent
from stack import *

def dfs(graph, start, visited=None, parent=None, print_steps=True):
    if visited is None:
        visited = set()
    
    visited.add(start)
    
    is_acyclic = True 
    
    for neighbor in adjacent(graph, start):
        if neighbor not in visited:
            print(f"go to {neighbor}") if print_steps else None

            child_is_acyclic, _ = dfs(graph, neighbor, visited, parent=start, print_steps=print_steps)
            
            if not child_is_acyclic:
                is_acyclic = False

            print(f"go to {start}") if print_steps else None
            
        elif parent is not None and neighbor != parent:
            is_acyclic = False

    return is_acyclic, visited

def bfs(graph, node):
    pred = {node: None}
    dist = {node: 0}
    queue = [node]  
    while queue:
        current = queue.pop(0)
        for neighbor in adjacent(graph, current):
            if neighbor not in dist:
                pred[neighbor] = current
                dist[neighbor] = dist[current] + 1
                queue.append(neighbor)
    return pred, dist

def dfsIterative(graph, start):
    stack = Stack()
    visited = set()

    stack.push(start)

    while not stack.is_empty():
        node = stack.pop()

        if node not in visited:
            visited.add(node)

            for neighbor in adjacent(graph, node):
                if neighbor not in visited:
                    stack.push(neighbor)

    return visited