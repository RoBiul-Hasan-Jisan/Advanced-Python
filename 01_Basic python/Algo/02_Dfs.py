from collections import defaultdict, deque


graph = defaultdict(list)

edge = int(input("Enter number of edges: "))

print("Enter edges (u v):")
for _ in range(edge):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)  # remove this line for directed graph



def dfs(graph, node, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(node)
    path.append(node)

    if node == end:
        print(" DFS Path:", " -> ".join(path))
        return path

    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, end, visited, path.copy())
            if result:
                return result

    return None



print("\nGraph Representation:")
for node in graph:
    print(f"{node} -> {graph[node]}")





start = input("\nEnter starting node: ")
end = input("Enter ending node: ")



dfs(graph, start, end)