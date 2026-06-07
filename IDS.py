def depth_limited_search(graph, node, goal, depth, path):
    print(f"Visiting: {node} | Remaining Depth: {depth}")

    path.append(node)

    if node == goal:
        print("\nGoal Found!")
        print("Path:", " -> ".join(path))
        return True

    if depth == 0:
        path.pop()
        return False

    for neighbor in graph[node]:
        if depth_limited_search(graph, neighbor, goal, depth - 1, path):
            return True

    path.pop()
    return False


def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\n{'='*50}")
        print(f"Searching with Depth Limit = {depth}")
        print(f"{'='*50}")

        path = []

        if depth_limited_search(graph, start, goal, depth, path):
            print(f"\nGoal found at depth {depth}")
            return

    print("\nGoal Not Found within maximum depth.")


# Input Graph
graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("\nEnter node name: ")
    neighbors = input(
        f"Enter neighbors of {node} (space separated): "
    ).split()

    graph[node] = neighbors

start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")
max_depth = int(input("Enter Maximum Depth: "))

ids(graph, start, goal, max_depth)