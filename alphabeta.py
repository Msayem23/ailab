

import heapq

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))

    g_cost = {start: 0}

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            print("\nGoal Found!")
            print("Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        for neighbor, cost in graph[current]:
            new_g = g + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    print("Goal Not Found")


# Input Section
graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("\nEnter node name: ")
    m = int(input(f"How many neighbors of {node}? "))

    graph[node] = []

    for _ in range(m):
        neighbor = input("Enter neighbor name: ")
        cost = int(input(f"Enter cost from {node} to {neighbor}: "))
        graph[node].append((neighbor, cost))

heuristic = {}

print("\nEnter heuristic values:")
for node in graph:
    heuristic[node] = int(input(f"h({node}) = "))

start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")

a_star(graph, heuristic, start, goal)