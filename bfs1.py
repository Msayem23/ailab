from collections import deque

def breadth_first_search(network, source, destination):
    waiting_list = deque([(source, [source])])
    explored = {source}

    print("\n===== Breadth First Search =====\n")

    while waiting_list:

        current_vertex, route = waiting_list.popleft()

        print("Visiting Node:", current_vertex)
        print("Route So Far:", " -> ".join(route))

        if current_vertex == destination:
            print("\nDestination Reached!")
            print("Shortest Route:", " -> ".join(route))
            return

        for next_vertex in network[current_vertex]:
            if next_vertex not in explored:
                explored.add(next_vertex)
                waiting_list.append(
                    (next_vertex, route + [next_vertex])
                )
                print(f"Inserted {next_vertex} into queue")

        print("-" * 35)

    print("No Route Available")


# Graph Input
network = {}

total_nodes = int(input("How many nodes? "))

for i in range(total_nodes):
    vertex = input(f"\nNode {i+1} name: ")

    adjacent = input(
        f"Connected nodes of {vertex} (space separated): "
    ).split()

    network[vertex] = adjacent

source = input("\nStarting Node: ")
destination = input("Destination Node: ")

breadth_first_search(network, source, destination)