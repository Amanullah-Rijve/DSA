def prim(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True  # start from node 0

    edges = 0
    total_cost = 0

    while edges < n - 1:
        minimum = float('inf')
        x = y = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"Edge: {x} - {y}  Cost: {graph[x][y]}")
        total_cost += graph[x][y]
        selected[y] = True
        edges += 1

    print("Total cost:", total_cost)


# Example (Adjacency Matrix)
graph = [
    [0, 2, 3, 0],
    [2, 0, 1, 4],
    [3, 1, 0, 5],
    [0, 4, 5, 0]
]

prim(graph)