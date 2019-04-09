"""
Simple graph implementation
"""
from collections import deque


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, vert1, vert2):
        if vert1 in self.vertices and vert2 in self.vertices:
            self.vertices[vert1].add(vert2)
            self.vertices[vert2].add(vert1)
        else:
            raise IndexError("That vertex does not exist.")

    def add_directed_edge(self, vert1, vert2):
        if vert1 in self.vertices and vert2 in self.vertices:
            self.vertices[vert1].add(vert2)
        else:
            raise IndexError("That vertex does not exist.")

    def dft(self, starting_vert):
        visited = set()
        stack = []
        stack.append(starting_vert)

        while stack:
            vert = stack.pop()
            if vert not in visited:
                visited.add(vert)
                print(vert)
                for edge in self.vertices[vert]:
                    stack.append(edge)

    def dft_rec(self, starting_vert, visited=set()):
        if starting_vert in visited:
            return
        else:
            visited.add(starting_vert)
            print(starting_vert)
            for vert in self.vertices[starting_vert]:
                self.dft_rec(vert, visited)

    def bft(self, starting_vert):
        visited = set()
        queue = deque()
        queue.append(starting_vert)

        while queue:
            vert = queue.popleft()
            if vert not in visited:
                visited.add(vert)
                print(vert)
                for edge in self.vertices[vert]:
                    queue.append(edge)
