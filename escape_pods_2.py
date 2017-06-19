# Escape Pods
from collections import deque


def bfs(start, end, path, flows):
    length = len(path)
    parents = [-1] * length     # parent table for reverse tracing path
    parents[start] = -2         # differentiate start point from others

    queue = deque()
    queue.append(start)
    while queue and parents[end] == -1:
        u = queue.popleft()
        for v in range(length):
            cf = path[u][v] - flows[u][v]
            if cf > 0 and parents[v] == -1:
                queue.append(v)
                parents[v] = u

    if parents[end] == -1:      # if t can not been reached
        return 0, parents

    v = end
    delta = float('Inf')
    while v != start:
        u = parents[v]
        cf = path[u][v] - flows[u][v]
        delta = min(delta, cf)
        v = u

    return delta, parents


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
    transform(path, entrances, exits)
    flow = 0
    length = len(path)
    flows = [[0 for _ in range(length)] for __ in range(length)]
    start = 0
    end = length - 1
    while True:
        ap_flow, parents = bfs(start, end, path, flows)
        if ap_flow == 0:
            break
        flow += ap_flow
        v = end
        while v != start:
            u = parents[v]
            flows[u][v] += ap_flow
            flows[v][u] -= ap_flow
            v = u
    return flow


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

print(answer(*case1))
