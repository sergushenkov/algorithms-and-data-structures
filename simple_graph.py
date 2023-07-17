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
        vertex_index = VFrom
        checked_vertex = {vertex_index}
        steak.append(self.vertex[vertex_index])
        while steak:
            is_neighbor = False
            for neighbor, is_edge in enumerate(self.m_adjacency[vertex_index]):
                if not is_edge or neighbor in checked_vertex:
                    continue
                if VTo == neighbor:
                    steak.append(self.vertex[VTo])
                    return steak
                checked_vertex.add(neighbor)
                steak.append(self.vertex[neighbor])
                is_neighbor = True
                vertex_index = neighbor
                break
            if not is_neighbor:
                next_vertex = steak.pop()
                vertex_index = self.vertex.index(next_vertex)
        return []

    def BreadthFirstSearch(self, VFrom, VTo):
        step = Step(VFrom, [self.vertex[VFrom]])
        queue = Queue(step)
        checked_vertex = set()
        while queue.first is not None:
            current_vertex = queue.push_first()
            path = current_vertex.path
            checked_vertex.add(current_vertex.vertex_i)
            for vertex_index, is_edge in enumerate(self.m_adjacency[current_vertex.vertex_i]):
                if not is_edge or vertex_index in checked_vertex:
                    continue
                if vertex_index == VTo:
                    path.append(self.vertex[vertex_index])
                    return path
                next_path = path.copy()
                next_path.append(self.vertex[vertex_index])
                next_vertex = Step(vertex_index, next_path)
                queue.add_last(next_vertex)
        return []

    def WeakVertices(self):
        weak_vertices = []
        for vertex_index, vertex in enumerate(self.vertex):
            neighbors = set()
            for neighbor_i, is_edge in enumerate(self.m_adjacency[vertex_index]):
                if is_edge:
                    neighbors.add(neighbor_i)
            for neighbor_i, row in enumerate(self.m_adjacency):
                if row[vertex_index] == 1:
                    neighbors.add(neighbor_i)
            neighbors.discard(vertex_index)
            is_weak_vertix = True
            while neighbors:
                first_neighbor = neighbors.pop()
                for neighbor_i, is_edge in enumerate(self.m_adjacency[first_neighbor]):
                    if (is_edge and neighbor_i != first_neighbor
                            and neighbor_i in neighbors):
                        is_weak_vertix = False
                        break
                for neighbor_i, row in enumerate(self.m_adjacency):
                    if (row[first_neighbor] == 1 and neighbor_i != first_neighbor
                            and neighbor_i in neighbors):
                        is_weak_vertix = False
                        break
            if is_weak_vertix:
                weak_vertices.append(vertex)

        return weak_vertices
