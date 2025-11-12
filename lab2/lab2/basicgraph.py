import random

def read_graph(filename):
    graph = {}
    with open(filename,'r') as f:
        for line in f:
            parts = line.strip().split(':')
            node = parts[0].strip()
            neighbors = []
            if len(parts) > 1:
                for n in parts[1].split(','):
                    neighbors.append(n.strip())
            graph[node] = neighbors
    return graph

def adjacent(graph,node):
    return iter(graph[node])

def random_node(graph):
    return random.choice(list(graph.keys()))

def main():
    filepath = input('Enter file path: ')
    graph = read_graph(filepath)
    print(graph)
    v = random_node(graph)
    print('a random node:', v)
    print('the adjacent of',v,':')
    for a in adjacent(graph,v):
        print(a, end=' ')

if __name__ == '__main__':
    main()
