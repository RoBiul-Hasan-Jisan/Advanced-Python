from collections import deque

graph = {}
n = int(input("Nodes: "))

for i in range(n):
    node = input("Node: ")
    graph[node] = input("Neighbors: ").split()

start = input("Start: ")
end = input("End: ")

q = deque([start])
visited = []

while q:
    x = q.popleft()

    if x not in visited:
        print(x, end=" ")
        visited.append(x)

        if x == end:   # stop when end is found
            break

        q += graph[x]