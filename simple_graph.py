class Step:

    def __init__(self, vertex_index, path):
        self.vertex_i = vertex_index
        self.path = path
        self.next = None


class Queue:

    def __init__(self, first=None):
        self.first = first

    def add_last(self, new_last):
        if self.first is None:
            self.first = new_last
            return
        current_last = self.first
        while current_last.next is not None:
            current_last = current_last.next
        current_last.next = new_last

    def push_first(self):
        current_first = self.first
        self.first = self.first.next
        return current_first


class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, value):
        new_vertex = Vertex(value)
        is_free_space = False
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                new_vertex_index = i
                is_free_space = True
                break
        if is_free_space:
            self.vertex[new_vertex_index] = new_vertex

    def RemoveVertex(self, vertex_index):
        self.vertex[vertex_index] = None
        for i in range(self.max_vertex):
            self.RemoveEdge(i, vertex_index)
            self.RemoveEdge(vertex_index, i)

    def IsEdge(self, vertex_index_1, vertex_index_2):
        return self.m_adjacency[vertex_index_1][vertex_index_2] == 1

    def AddEdge(self, vertex_index_1, vertex_index_2):
        self.m_adjacency[vertex_index_1][vertex_index_2] = 1
        # self.m_adjacency[vertex_index_2][vertex_index_1] = 1

    def RemoveEdge(self, vertex_index_1, vertex_index_2):
        self.m_adjacency[vertex_index_1][vertex_index_2] = 0
        # self.m_adjacency[vertex_index_2][vertex_index_1] = 0

    def DepthFirstSearch(self, VFrom, VTo):
        steak = []
        vertex = VFrom
        checked_vertex = {vertex}
        steak.append(vertex)
        while steak:
            neighbors = set()
            for next_vertex, is_edge in enumerate(self.m_adjacency[vertex]):
                if is_edge and next_vertex not in checked_vertex:
                    neighbors.add(next_vertex)
            if VTo in neighbors:
                steak.append(VTo)
                path = []
                for vertex_index in steak:
                    path.append(self.vertex[vertex_index])
                return path
            if neighbors:
                vertex = neighbors.pop()
                checked_vertex.add(vertex)
                steak.append(vertex)
                continue
            vertex = steak.pop()
        return []

    def BreadthFirstSearch(self, VFrom, VTo):
        step = Step(VFrom, [VFrom])
        queue = Queue(step)
        checked_vertex = set()
        while queue.first is not None:
            current_vertex = queue.push_first()
            path = current_vertex.path
            checked_vertex.add(current_vertex.vertex_i)
            for vertex, is_nearby in enumerate(self.m_adjacency[current_vertex.vertex_i]):
                if not is_nearby or vertex in checked_vertex:
                    continue
                if vertex == VTo:
                    path.append(vertex)
                    result = []
                    for vertex_index in path:
                        result.append(self.vertex[vertex_index])
                    return result
                next_path = path.copy()
                next_path.append(vertex)
                next_vertex = Step(vertex, next_path)
                queue.add_last(next_vertex)
        return []
