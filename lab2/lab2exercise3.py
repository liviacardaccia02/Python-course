from basicgraph import read_graph, random_node
from algorithms import dfs

def is_acyclic(graph):
    is_acyclic = dfs(graph, random_node(graph), visited=None, parent=None, print_steps=False)[0]
    return is_acyclic

def main():
    filepath = input("Enter the file path: ")
    graph = read_graph(filepath)
    if is_acyclic(graph):
        print("Cyclic graph")
    else:
        print("Non-acyclic graph")

if __name__ == "__main__":
    main()

