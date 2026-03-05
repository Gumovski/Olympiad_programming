import graphviz

# Данные графа
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

def visualize_with_graphviz(graph_data):
    directed = is_directed(graph_data)

    if directed:
        dot = graphviz.Digraph(comment='Graph', engine='neato')
    else:
        dot = graphviz.Graph(comment='Graph', engine='neato')

    dot.attr(overlap='false', splines='true')
    dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')

    for u, neighbors in graph_data.items():
        dot.node(str(u))

    if directed:
        for u, neighbors in graph_data.items():
            for v, weight in neighbors:
                dot.edge(str(u), str(v), label=str(weight))
    else:
        added_edges = set()
        for u, neighbors in graph_data.items():
            for v, weight in neighbors:
                edge_key = tuple(sorted((str(u), str(v))))
                if edge_key not in added_edges:
                    dot.edge(str(u), str(v), label=str(weight))
                    added_edges.add(edge_key)

    try:
        output_path = dot.render('graph-output', format='png', view=True)
        print(f"Граф сохранен: {output_path}")
    except Exception as e:
        print(f"Ошибка при рендеринге: {e}")
        print("Убедитесь, что Graphviz установлен в системе и добавлен в PATH.")

if __name__ == '__main__':
    visualize_with_graphviz(graph_data)
