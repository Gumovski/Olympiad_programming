import networkx as nx
import matplotlib.pyplot as plt

# Граф из файла "Алгоритм Дейкстры.py"
graph_data = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('B', 2), ('A', 4), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

def visualize_graph(graph_data):
    # Создаем граф
    G = nx.Graph()

    # Добавляем ребра
    for node, neighbors in graph_data.items():
        for neighbor, weight in neighbors:
            # В networkx для неориентированного графа ребро добавляется один раз
            # но повторное добавление с тем же весом не вызовет ошибки
            G.add_edge(node, neighbor, weight=weight)

    # Выбираем раскладку (расположение узлов)
    pos = nx.spring_layout(G, seed=42)  # seed для воспроизводимости

    plt.figure(figsize=(8, 6))

    # Рисуем узлы
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')

    # Рисуем метки узлов
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

    # Рисуем ребра
    nx.draw_networkx_edges(G, pos, width=2)

    # Рисуем веса ребер
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Визуализация графа")
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    visualize_graph(graph_data)