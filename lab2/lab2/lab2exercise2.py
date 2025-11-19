from basicgraph import *
from algorithms import dfs

def is_connected(graph):
    start = random_node(graph)
    visited_nodes = dfs(graph, start, visited=None, parent=None, print_steps=False)[1]
    return len(visited_nodes) == len(graph)

def main():
    filepath = input("Enter the file path: ")
    graph = read_graph(filepath)
    if is_connected(graph):
        print("Graph is connected")
    else:
        print("Graph is not connected")

if __name__ == "__main__":
    main()
