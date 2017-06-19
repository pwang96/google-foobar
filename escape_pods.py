# Escape Pods
from collections import deque


def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    q = deque()

    q.append(s)
    visited[s] = True

    while q:
        u = q.popleft()

        # Get all adjacent vertices's of the dequeued vertex u
        # If a adjacent has not been visited, then mark it
        # visited and enqueue it
        for ind, val in enumerate(graph[u]):
            if not visited[ind] and val > 0:
                q.append(ind)
                visited[ind] = True
                parent[ind] = u

    return visited[t]


def edmondskarp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


def transform(graph, entrances, exits):
    n = len(graph)
    entrances = [i + 1 for i in entrances]
    exits = [i + 1 for i in exits]

    graph.insert(0, [float('Inf') if i in entrances else 0 for i in range(n + 2)])
    for i in range(1, n + 1):
        graph[i] = [0] + graph[i] + [float('Inf') if i in exits else 0]
    graph.append([0] * (n + 2))

    return graph, entrances, exits


def answer(entrances, exits, path):
    if len(entrances) > 1 or len(exits) > 1:
        path, entrances, exits = transform(path, entrances, exits)

    if len(path) == 0:
        return 0

    return edmondskarp(path, 0, len(path) - 1)


g1 = [[0, 0, 4, 6, 0, 0],
     [0, 0, 5, 2, 0, 0],
     [0, 0, 0, 0, 4, 4],
     [0, 0, 0, 0, 6, 6],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

g2 = [[0, 7, 0, 0],
      [0, 0, 6, 0],
      [0, 0, 0, 8],
      [9, 0, 0, 0]]

g3 = [[0, 0, 0, 4, 6, 0],
      [0, 0, 0, 5, 2, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 4, 0, 0, 4],
      [0, 0, 6, 0, 0, 6],
      [0, 0, 0, 0, 0, 0]]

case1 = ([0, 1], [4, 5], g1)
case2 = ([0], [3], g2)
case3 = ([0, 1], [2, 5], g3)

print(answer(*case3))
