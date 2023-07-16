from simple_graph import SimpleGraph


def test_init():
    graph = SimpleGraph(5)
    assert graph.max_vertex == 5
    assert len(graph.m_adjacency) == 5
    assert len(graph.m_adjacency[0]) == 5
    assert len(graph.vertex) == 5


def test_add_vertex():
    graph = SimpleGraph(5)
    assert graph.vertex[0] is None
    graph.AddVertex(20)
    assert graph.vertex[0].Value == 20
    assert graph.vertex[1] is None

    for i, number in enumerate((21, 22, 23, 24)):
        graph.AddVertex(number)
        assert graph.vertex[i + 1].Value == number
    for i, number in enumerate((20, 21, 22, 23, 24)):
        assert graph.vertex[i].Value == number

    graph.AddVertex(25)
    for i, number in enumerate((20, 21, 22, 23, 24)):
        assert graph.vertex[i].Value == number


def test_add_edge():
    graph = SimpleGraph(3)
    for number in (10, 11, 12):
        graph.AddVertex(number)
    assert graph.m_adjacency[0][1] == 0
    assert graph.m_adjacency[1][0] == 0
    graph.AddEdge(1, 0)
    assert graph.m_adjacency[0][1] == 0
    assert graph.m_adjacency[1][0] == 1
    assert graph.m_adjacency[2][1] == 0
    assert graph.m_adjacency[1][2] == 0
    graph.AddEdge(1, 2)
    assert graph.m_adjacency[1][2] == 1
    assert graph.m_adjacency[2][1] == 0
    graph.AddEdge(2, 2)
    assert graph.m_adjacency[1][2] == 1
    assert graph.m_adjacency[2][1] == 0
    assert graph.m_adjacency[0][1] == 0
    assert graph.m_adjacency[1][0] == 1
    assert graph.m_adjacency[0][2] == 0
    assert graph.m_adjacency[2][0] == 0
    assert graph.m_adjacency[0][0] == 0
    assert graph.m_adjacency[1][1] == 0
    assert graph.m_adjacency[2][2] == 1


def test_remove_edge():
    graph = SimpleGraph(3)
    for number in (10, 11, 12):
        graph.AddVertex(number)
    graph.AddEdge(1, 0)
    assert graph.m_adjacency[0][1] == 0
    assert graph.m_adjacency[1][0] == 1
    graph.RemoveEdge(1, 0)
    assert graph.m_adjacency[0][1] == 0
    assert graph.m_adjacency[1][0] == 0


def test_is_edge():
    graph = SimpleGraph(3)
    for number in (10, 11, 12):
        graph.AddVertex(number)
    assert graph.IsEdge(1, 0) is False
    graph.AddEdge(1, 0)
    assert graph.IsEdge(1, 0) is True
    assert graph.IsEdge(0, 1) is False
    graph.AddEdge(0, 1)
    assert graph.IsEdge(1, 0) is True
    assert graph.IsEdge(0, 1) is True
    graph.RemoveEdge(1, 0)
    assert graph.IsEdge(1, 0) is False
    assert graph.IsEdge(0, 1) is True


def test_remove_vertex():
    graph = SimpleGraph(4)
    for number in (10, 11, 12, 13):
        graph.AddVertex(number)
    assert graph.vertex[1].Value == 11
    graph.RemoveVertex(1)
    assert graph.vertex[1] is None

    graph.AddEdge(0, 2)
    graph.AddEdge(2, 2)
    graph.AddEdge(2, 3)
    graph.AddEdge(0, 3)
    assert graph.IsEdge(0, 2) is True
    assert graph.IsEdge(2, 2) is True
    assert graph.IsEdge(2, 3) is True
    assert graph.IsEdge(0, 3) is True
    graph.RemoveVertex(2)
    assert graph.vertex[2] is None
    assert graph.IsEdge(0, 2) is False
    assert graph.IsEdge(2, 2) is False
    assert graph.IsEdge(2, 3) is False
    assert graph.IsEdge(0, 3) is True


def test_depth_first_search():
    graph = SimpleGraph(6)
    for number in (10, 11, 12, 13, 14, 15):
        graph.AddVertex(number)
    for edge in ((1, 2), (1, 3), (2, 3), (3, 4), (4, 5)):
        graph.AddEdge(*edge)
    assert graph.DepthFirstSearch(0, 1) == []
    assert graph.DepthFirstSearch(1, 2) == [1, 2]
    assert graph.DepthFirstSearch(2, 1) == []
    assert graph.DepthFirstSearch(2, 5) == [2, 3, 4, 5]
    graph.AddEdge(2, 1)
    assert graph.DepthFirstSearch(1, 2) == [1, 2]
    assert graph.DepthFirstSearch(2, 1) == [2, 1]
    graph.AddEdge(2, 3)
    assert graph.DepthFirstSearch(2, 5) == [2, 1, 3, 4, 5]
