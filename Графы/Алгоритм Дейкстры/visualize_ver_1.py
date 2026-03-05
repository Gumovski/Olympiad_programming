import networkx as nx
import matplotlib.pyplot as plt

# Граф из файла "Алгоритм Дейкстры.py"
graph_data = {
    'A': [('B', 1), ('C', -4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('B', 2), ('A', -4), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
    'E': [('C', 1)],
}

def is_directed(graph_data):
    for u, neighbors in graph_data.items():
        for v, w in neighbors:
            reverse_exists = any(n == u and wt == w for n, wt in graph_data.get(v, []))
            if not reverse_exists:
                return True
    return False

def visualize_graph(graph_data):
    directed = is_directed(graph_data)

    G = nx.DiGraph() if directed else nx.Graph()

    for node, neighbors in graph_data.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))

    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

    if directed:
        nx.draw_networkx_edges(G, pos, width=2, arrows=True, arrowstyle='->', arrowsize=20)
    else:
        nx.draw_networkx_edges(G, pos, width=2)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Визуализация графа (ориентированный)" if directed else "Визуализация графа (неориентированный)")
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    visualize_graph(graph_data)