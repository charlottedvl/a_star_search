class Node:
    # Definition of a node
    def __init__(self, name="", h=0):
        self.name = name
        self.h = h

    # Computation of f cost
    def f(self, g):
        return self.h + g


class Graph:
    # Definition of a graph
    def __init__(self, successors):
        self.successors_list = successors

    # Find all successors for a given node
    def find_successors(self, node):
        return self.successors_list[node]


def a_star_search(graph, starting_node, goal_node):
    # Initialize fringe and closed arrays
    fringe = [starting_node]
    closed = []

    # List of minimum g_cost to get to node n from start
    g_cost = {starting_node: 0}

    # Initialize the f_cost of the starting node
    f_cost = {starting_node: starting_node.f(g_cost[starting_node])}

    # Map of parents for each node
    parents = {starting_node: None}

    # While the fringe isn't empty
    while fringe:
        # Initiate the current node
        current_node = None

        # Search the node with the lowest f_cost
        for node in fringe:
            # Compare the f cost of the node to the f cost of the current node if it exists
            if current_node is None or f_cost[node] < f_cost[current_node]:
                current_node = node
            # If two f_cost are equals, then choose by alphabetical order the current_node
            elif f_cost[node] == f_cost[current_node] and node.name < current_node.name:
                current_node = node

        # Test if it is the goal node
        if current_node == goal_node:
            # Construct the path
            path_found = []
            while current_node:
                path_found.append(current_node)
                current_node = parents[current_node]
            # Rearrange the path to have from start node to goal node
            path_found.reverse()

            print("Parsed nodes: ", end=" ")
            # Print each parsed node
            for index, node in enumerate(closed):
                print(node.name, end="")
                # Add " - " if it isn't the last node of the closed list
                if index < len(closed) - 1:
                    print(" - ", end="")

            print("\nPath found: ", end=" ")
            # Print each node of the path
            for node in path_found:
                # If it is the goal node, then don't add the " - " at the end
                if node.name != goal_node.name:
                    print(node.name, end=" - ")
                else:
                    print(node.name)
            return path_found

        # Remove the node from the list fringe
        fringe.remove(current_node)

        # Find successors
        successors = graph.find_successors(current_node)
        for (successor, weight) in successors:
            # Check if the node is in closed
            # If the node is in closed, it means that a previous path with lower f_cost has been found
            if successor not in closed:
                # Compute the g cost
                g_cost[successor] = g_cost[current_node] + weight
                # If the successor has already been found as a successor of another node
                # And if the cost to get to the successor is less than the previous found
                # Then update the f_cost
                if successor not in f_cost or successor.f(g_cost[successor]) <= f_cost[successor]:
                    f_cost[successor] = successor.f(g_cost[successor])
                    # Get track of the parent of the successor
                    parents[successor] = current_node
                # Add the successor to the fringe
                if successor not in fringe:
                    fringe.append(successor)

        # Add the current_node to closed
        closed.append(current_node)
    # If we reach this point, it means that there no path retrieved that leads to goal
    print("No path found")
    return None


# Creating the nodes
start_node = Node("Start", 0)
A_node = Node("A", 2)
B_node = Node("B", 5)
C_node = Node("C", 2)
D_node = Node("D", 1)
goal_node = Node("Goal", 0)

# Creating the list of successors for each node
successors_list = {
    start_node: [(A_node, 2), (B_node, 3), (D_node, 5)],
    A_node: [(start_node, 2), (C_node, 4)],
    B_node: [(start_node, 3), (D_node, 4)],
    C_node: [(A_node, 4), (D_node, 1), (goal_node, 2)],
    D_node: [(start_node, 5), (B_node, 4), (C_node, 1), (goal_node, 5)],
    goal_node: [(C_node, 2), (D_node, 5)]
}

# Creating the graph
graph_given = Graph(successors_list)

# Performing the A* search
path = a_star_search(graph_given, start_node, goal_node)
