from basicgraph import adjacent

def dfs(graph, start, visited, parent):
    visited.add(start)
    for neighbor in adjacent(graph, start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, parent=start)
        elif parent is not None and neighbor != parent:
            return False # cycle detected
    return True