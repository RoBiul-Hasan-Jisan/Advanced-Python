def find_path(parent, node):
    path = [node]
    while node in parent:
        path.append(parent[node])
        node = parent[node]
    return path[::-1]

import heapq

def a_star(graph, h, start, goal):
    open_list = []
    heapq.heappush(open_list, (h[start], 0, start))  # (f = g + h, g, node)
    parent = {}
    g_score = {start: 0}
    visited = set()

    while open_list:
        f, g, cur_node = heapq.heappop(open_list)

        if cur_node == goal:
            return find_path(parent, cur_node)

        if cur_node in visited:
            continue
        visited.add(cur_node)

        for neighbor, cost in graph[cur_node].items():
            tentative_g = g + cost
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h[neighbor]
                heapq.heappush(open_list, (f_score, tentative_g, neighbor))
                parent[neighbor] = cur_node

    return None 


n = int(input("Enter number of nodes: "))

graph = {}
for _ in range(n):
    node = input("Enter node name: ")
    neighbors_input = input(f"Enter neighbors of {node} with costs (format: neighbor:cost, space separated): ").replace(",", "").split()
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


path = a_star(graph, h, start, goal)
if path:
    print("A* Path:", path)
else:
    print("No path found from", start, "to", goal)