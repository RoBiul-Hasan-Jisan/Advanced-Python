from collections import defaultdict, deque


graph = defaultdict(list)

edge = int(input("Enter number of edges: "))

print("Enter edges (u v):")
for _ in range(edge):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)  # remove this line for directed graph



def bfs(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])

    visited.add(start)

    while queue:
        node, path = queue.popleft()

        if node == end:
            print(" BFS Shortest Path:", " -> ".join(path))
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    print(" No path found using BFS")
    return None




print("\nGraph Representation:")
for node in graph:
    print(f"{node} -> {graph[node]}")





start = input("\nEnter starting node: ")
end = input("Enter ending node: ")


bfs(graph, start, end)
