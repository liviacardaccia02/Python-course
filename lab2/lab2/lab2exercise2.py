from basicgraph import *
from algorithms import dfs

def is_connected(graph):
    visited = set()
    start = random_node(graph)
    dfs(graph, start, visited, parent=None)
    return len(visited) == len(graph)

def main():
    filepath = input("Enter the file path: ")
    graph = read_graph(filepath)
    if is_connected(graph):
        print("Graph is connected")
    else:
        print("Graph is not connected")

if __name__ == "__main__":
    main()
