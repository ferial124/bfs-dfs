def bfs(graph, start, goal):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
    else:
        adjacent_nodes = graph.get(node, [])
        for node2 in adjacent_nodes:
            if node2 not in path:
                new_path = list(path)
                new_path.append(node2)
                queue.append(new_path)


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)


Return
visited
