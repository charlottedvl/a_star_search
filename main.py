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
    return None
