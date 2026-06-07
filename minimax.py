def minimax(depth, node_index, is_max, values, max_depth):
    
    # If leaf node reached
    if depth == max_depth:
        print(f"Leaf Node {node_index}: Value = {values[node_index]}")
        return values[node_index]

    if is_max:
        print(f"\nMAX at Node {node_index}")

        left = minimax(depth + 1, node_index * 2,
                       False, values, max_depth)

        right = minimax(depth + 1, node_index * 2 + 1,
                        False, values, max_depth)

        result = max(left, right)

        print(f"MAX chooses max({left}, {right}) = {result}")

        return result

    else:
        print(f"\nMIN at Node {node_index}")

        left = minimax(depth + 1, node_index * 2,
                       True, values, max_depth)

        right = minimax(depth + 1, node_index * 2 + 1,
                        True, values, max_depth)

        result = min(left, right)

        print(f"MIN chooses min({left}, {right}) = {result}")

        return result


# Input
depth = int(input("Enter tree depth: "))

num_leaf_nodes = 2 ** depth

print(f"Enter {num_leaf_nodes} leaf node values:")

values = []

for i in range(num_leaf_nodes):
    value = int(input(f"Leaf {i}: "))
    values.append(value)

print("\n===== Minimax Execution =====")

optimal_value = minimax(
    0,          # current depth
    0,          # root node index
    True,       # MAX starts first
    values,
    depth
)

print("\nOptimal Value:", optimal_value)