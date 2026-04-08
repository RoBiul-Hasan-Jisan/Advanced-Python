def find_path(parent, node):
    path = [node]
    while node in parent:
        path.append(parent[node])
        node = parent[node]
    return path[::-1]

def greedyBFS(graph, h, start, goal):
    open_list = [(start, h[start])]  # (node, heuristic)
    visited = set()
    parent = {}

    while open_list:
        # Sort by heuristic value (smallest first)
        open_list.sort(key=lambda x: x[1])
        cur_node, h_value = open_list.pop(0)

        if cur_node not in visited:
            visited.add(cur_node)

            if cur_node == goal:
                return find_path(parent, cur_node)

            for neighbor in graph[cur_node]:  # graph[cur_node] is a dict {neighbor: cost}
                if neighbor not in visited:
                    open_list.append((neighbor, h[neighbor]))
                    parent[neighbor] = cur_node

    return None  # if no path found


n = int(input("Enter number of nodes: "))

graph = {}
for _ in range(n):
    node = input("Enter node name: ")
    neighbors_input = input(f"Enter neighbors of {node} with costs (format: neighbor:cost, space separated): ").split()
    graph[node] = {}
    for item in neighbors_input:
        neighbor, cost = item.split(":")
        graph[node][neighbor] = float(cost)

h = {}
print("Enter heuristic values for each node:")
for node in graph:
    h[node] = float(input(f"h({node}) = "))

start = input("Enter starting node: ")
goal = input("Enter goal node: ")


path = greedyBFS(graph, h, start, goal)
if path:
    print("Greedy BFS Path:", path)
else:
    print("No path found from", start, "to", goal)