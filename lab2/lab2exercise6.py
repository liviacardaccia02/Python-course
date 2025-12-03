from basicgraph import read_graph
from lab2exercise5 import bfs

def radius(graph): 
    if not graph:
        return 0
    
    start_node = next(iter(graph))
    _, dist_from_start = bfs(graph, start_node)
    
    node_a = max(dist_from_start, key=dist_from_start.get)
    _, dist_from_a = bfs(graph, node_a)
    max_distance = max(dist_from_a.values())
    
    return max_distance

def main():
    filepath = input("Enter the file path: ")
    graph = read_graph(filepath)
    print("radius is", radius(graph))

if __name__ == "__main__":
    main()
