from basicgraph import read_graph, random_node
from algorithms import dfs

def is_acyclic(graph):
    return dfs(graph, random_node(graph), set(), parent=None)

def main():
    filepath = input("Enter the file path: ")
    graph = read_graph(filepath)
    if is_acyclic(graph):
        print("Cyclic graph")
    else:
        print("Non-acyclic graph")

if __name__ == "__main__":
    main()

