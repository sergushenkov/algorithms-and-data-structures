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
        if self.m_adjacency[vertex_index_1][vertex_index_2] == 1:
            return True
        return False

    def AddEdge(self, vertex_index_1, vertex_index_2):
        self.m_adjacency[vertex_index_1][vertex_index_2] = 1
        # self.m_adjacency[vertex_index_2][vertex_index_1] = 1

    def RemoveEdge(self, vertex_index_1, vertex_index_2):
        self.m_adjacency[vertex_index_1][vertex_index_2] = 0
        # self.m_adjacency[vertex_index_2][vertex_index_1] = 0
