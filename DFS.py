def dfs(graph, node, goal, visited, path):
    print(f"\nVisiting Node: {node}")

    visited.add(node)
    path.append(node)

    print("Current Path:", " -> ".join(path))
    print("Visited Nodes:", visited)

    if node == goal:
        print("\nGoal Found!")
        print("Final Path:", " -> ".join(path))
        return True

    for neighbor in graph[node]:
        if neighbor not in visited:
            print(f"Going to: {neighbor}")
            
            if dfs(graph, neighbor, goal, visited, path):
                return True

    print(f"Backtracking from: {node}")
    path.pop()

    return False


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

visited = set()
path = []

dfs(graph, start, goal, visited, path)