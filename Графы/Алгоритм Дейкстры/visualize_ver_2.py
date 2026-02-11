import graphviz

# Данные графа
graph_data = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('B', 2), ('A', 4), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

def visualize_with_graphviz(graph_data):
    # Создаем объект неориентированного графа
    # engine='neato' или 'circo' обычно хорошо подходят для таких структур
    dot = graphviz.Graph(comment='Dijkstra Graph', engine='neato')

    # Настройки внешнего вида
    dot.attr(overlap='false', splines='true')
    dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')

    # Чтобы не дублировать ребра (A-B и B-A), будем запоминать добавленные
    added_edges = set()

    for u, neighbors in graph_data.items():
        # Добавляем узел
        dot.node(str(u))

        for v, weight in neighbors:
            # Создаем уникальный ключ для ребра (сортируем узлы, чтобы A-B и B-A были одинаковы)
            edge_key = tuple(sorted((str(u), str(v))))

            if edge_key not in added_edges:
                # Добавляем ребро с весом
                dot.edge(str(u), str(v), label=str(weight))
                added_edges.add(edge_key)

    # Рендеринг и просмотр
    try:
        # Сохранит как graph-output.png и откроет
        output_path = dot.render('graph-output', format='png', view=True)
        print(f"Граф сохранен: {output_path}")
    except Exception as e:
        print(f"Ошибка при рендеринге: {e}")
        print("Убедитесь, что Graphviz установлен в системе и добавлен в PATH.")

if __name__ == '__main__':
    visualize_with_graphviz(graph_data)
