from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])

    print("\n===== BFS Traversal =====\n")

    while queue:
        print(f"Current Queue: {[node for node, path in queue]}")

        node, path = queue.popleft()

        print(f"Selected Node: {node}")
        print(f"Current Path: {' -> '.join(path)}")

        if node == goal:
            print("\nGoal Found!")
            print("Final Path:", " -> ".join(path))
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                print(f"Added Neighbor: {neighbor}")

        print("-" * 40)

    print("Goal Not Found")


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

bfs(graph, start, goal)



# "C:\Users\Gaming\OneDrive - Eos\Desktop\project\ailab\.venv\Scripts\python.exe" "C:\Users\Gaming\OneDrive - Eos\Desktop\project\ailab\bfs1.py" 
# How many nodes? 2

# Node 1 name: a
# Connected nodes of a (space separated): b

# Node 2 name: b
# Connected nodes of b (space separated): 0

# Starting Node: a
# Destination Node: b

# ===== Breadth First Search =====

# Visiting Node: a
# Route So Far: a
# Inserted b into queue
# -----------------------------------
# Visiting Node: b
# Route So Far: a -> b

# Destination Reached!
# Shortest Route: a -> b

# Process finished with exit code 0
