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

    def bfs(self, starting_vert, target):
        queue = deque()
        visited = set()
        path = []
        path.append(starting_vert)
        queue.append(path)

        while queue:
            shortest_path = queue.popleft()
            if shortest_path[-1] == target:
                return shortest_path
            if shortest_path[-1] not in visited:
                visited.add(shortest_path[-1])

                for edge in self.vertices[shortest_path[-1]]:
                    new_path = shortest_path[:]
                    new_path.append(edge)
                    queue.append(new_path)

        return 'not found'

    def dfs(self, starting_vert, target):
        stack = deque()
        visited = set()
        path = []
        path.append(starting_vert)
        stack.append(path)

        while stack:
            shortest_path = stack.pop()
            if shortest_path[-1] == target:
                return shortest_path
            if shortest_path[-1] not in visited:
                visited.add(shortest_path[-1])

                for edge in self.vertices[shortest_path[-1]]:
                    new_path = shortest_path[:]
                    new_path.append(edge)
                    stack.append(new_path)

        return 'not found'

    def breadth_first_search(self, start, target):
        queue = [start]
        result = []

        while len(queue) > 0:
            currentVertex = queue.pop(0)
            result.append(currentVertex)
            if currentVertex == target:
                break
            else:
                for value in self.vertices[currentVertex]:
                    queue.append(value)
        return result

    def breadth_first_traversal(self, start):
        queue = [start]
        result = []
        visited = {}

        visited[start] = True
        while len(queue) != 0:
            currentVertex = queue.pop(0)
            result.append(currentVertex)

            for value in self.vertices[currentVertex]:
                if value not in visited:
                    visited[value] = True
                    queue.append(value)

        return result

    def depth_first_search(self, start, target):
        stack = [start]
        result = []
        visited = {}

        while len(stack) != 0:
            currentVertex = stack.pop()
            print(stack)
            result.append(currentVertex)
            if currentVertex == target:
                break
            else:
                for value in self.vertices[currentVertex]:
                    if value not in visited:
                        visited[value] = True
                        stack.append(value)
        return result
