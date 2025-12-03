from basicgraph import read_graph
from algorithms import dfsIterative

def main():
    filepath = input("Enter the file path: ")
    graph = read_graph(filepath)
    start = input("Enter the start node: ")
    print("Path is", dfsIterative(graph, start))

if __name__ == "__main__":
    main()