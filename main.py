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
    def find_successors(self, v):
        return self.successors_list[v]


def a_star_search(graph, starting_node, goal_node):
    fringe = [starting_node]
    closed = []

    # List of minimum g_cost to get to node n from start
    g_cost = {starting_node: 0}

    # Map of parents for each node
    parents = {starting_node: None}

    # While the fringe isn't empty
    while fringe:
        # Initiate the current node
        current_node = None

        # Search the node with the lowest f_cost
        for node in fringe:
            if current_node is None or node.f(g_cost[node]) < current_node.f(g_cost[current_node]):
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

            print("Parsed nodes:")
            for node in closed:
                # Print each one of the parsed nodes
                print("Node:", node.name)

            print("Path found")
            for node in path_found:
                # Print each node of the path
                print("Node:",
                      node.name)
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
                parents[successor] = current_node
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
