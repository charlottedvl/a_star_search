class Node:
    def __init__(self, name="", h=0):
        self.name = name
        self.h = h

    def f(self, g):
        return self.h + g


class Graph:
    def __init__(self, successors):
        self.successors_list = successors

    def find_successors(self, v):
        return self.successors_list[v]


def a_star_search(graph, starting_node, goal_node):
    fringe = [starting_node]
    closed = []

    g_cost = {starting_node: 0}

    parents = {starting_node: None}

    while fringe:
        current_node = None

        for node in fringe:
            if current_node is None or node.f(g_cost[node]) < current_node.f(g_cost[current_node]):
                current_node = node

        if current_node == goal_node:
            return print("Success")

        fringe.remove(current_node)

        successors = graph.find_successors(current_node)
        for (successor, weight) in successors:
            if successor not in closed:
                g_cost[successor] = g_cost[current_node] + weight
                parents[successor] = current_node
                if successor not in fringe:
                    fringe.append(successor)

        closed.append(current_node)
    print("No path found")
    return None
