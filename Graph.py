from math import sqrt


class Graph(object):
    """Graph class"""
    def __init__(self):
        self.vertices = set()
        self.adjacent = {}
        self.edges = []

    def add_vertex(self, vertex):
        """Add vertex to the graph."""
        self.vertices.add(vertex)
        """Add vertex to the graph."""
        if vertex not in self.adjacent:
            self.adjacent[vertex] = []

    def add_edge(self, v1, v2):
        """Add edge to the graph between vertices v1 and v2."""
        self.add_vertex(v1)
        self.add_vertex(v2)
        if v2 not in self.adjacent[v1]:
            self.adjacent[v1].append(v2)
        if v1 not in self.adjacent[v2]:
            self.adjacent[v2].append(v1)
        self.edges.append([v1, v2])

    def get_vertices(self):
        """Get all vertices of the graph."""
        return list(self.vertices)

    def get_adjacent(self, vertex):
        """Get list of adjacent vertices in the graph for the vertex"""
        if vertex in self.adjacent:
            return self.adjacent[vertex]
        return []

    def if_adjacent(self, v1, v2):
        """If v1 is adjacent to v2 returns True, otherwise returns False"""
        if v1 in self.adjacent[v2]:
            return True
        return False

    def remove_edge(self, v1, v2):
        """if v1 and v2 has edge between them, removes it and returns True, returns False otherwise"""
        if v2 in self.adjacent[v1]:
            self.adjacent[v1].remove(v2)
            self.adjacent[v2].remove(v1)
            try:
                self.edges.remove([v1, v2])
            except ValueError:
                self.edges.remove([v2, v1])
            return True
        return False

    def has_edge(self, v1, v2):
        """Returns True if there is an edge between vertices v1 and v2, False otherwise."""
        if v1 not in self.vertices or v2 not in self.vertices:
            return False
        return v2 in self.adjacent[v1]

    def get_edge_weight(self, v1, v2):
        """Returns distance from v1 to v2 op plot if v1 is adjacent to v2, otherwise returns False"""
        if v1 in self.adjacent[v2]:
            return sqrt((v2[0] - v1[0]) ** 2 + (v2[1] - v1[1]) ** 2)
        return False