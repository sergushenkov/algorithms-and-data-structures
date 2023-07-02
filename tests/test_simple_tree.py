import pytest
from simple_tree import SimpleTreeNode, SimpleTree

@pytest.fixture
def setup_only_root():
    root = SimpleTreeNode(0, None)
    tree = SimpleTree(root)
    return tree, root

@pytest.fixture
def setup_three_leaf(setup_only_root):
    root = SimpleTreeNode(0, None)
    tree = SimpleTree(root)
    node_1 = SimpleTreeNode(1, None)
    tree.AddChild(root, node_1)
    node_2 = SimpleTreeNode(2, None)
    tree.AddChild(root, node_2)
    node_3 = SimpleTreeNode(3, None)
    tree.AddChild(node_1, node_3)
    return tree, root

def test_init(setup_only_root):    
    tree, root = setup_only_root
    assert tree.Root is root
    assert root.NodeValue == 0
    assert root.Parent is None
    assert root.Children == []
    empty_tree = SimpleTree(None)
    assert empty_tree.Root is None

def test_add_child(setup_only_root):
    tree, root = setup_only_root
    node_1 = SimpleTreeNode(1, None)
    tree.AddChild(root, node_1)
    assert tree.Root is root
    assert root.NodeValue == 0
    assert root.Parent is None
    assert len(root.Children) == 1
    assert root.Children[0] is node_1
    assert node_1.NodeValue == 1
    assert node_1.Parent is root
    assert node_1.Children == []

    node_2 = SimpleTreeNode(2, None)
    tree.AddChild(root, node_2)
    assert tree.Root is root
    assert root.NodeValue == 0
    assert root.Parent is None
    assert len(root.Children) == 2
    assert root.Children[0] is node_1
    assert root.Children[1] is node_2
    assert node_2.NodeValue == 2
    assert node_2.Parent is root
    assert node_2.Children == []

    node_3 = SimpleTreeNode(3, None)
    tree.AddChild(node_1, node_3)
    assert tree.Root is root
    assert root.NodeValue == 0
    assert root.Parent is None
    assert len(root.Children) == 2
    assert root.Children[0] is node_1
    assert root.Children[1] is node_2
    assert node_2.NodeValue == 2
    assert node_2.Parent is root
    assert node_2.Children == []
    assert node_1.NodeValue == 1
    assert node_1.Parent is root
    assert len(node_1.Children) == 1
    assert node_1.Children[0] is node_3
    assert node_3.NodeValue == 3
    assert node_3.Parent is node_1
    assert node_3.Children == []

def test_delete_node(setup_three_leaf):
    tree, root = setup_three_leaf
    node_1, node_2 = root.Children
    tree.DeleteNode(node_1)
    assert tree.Root is root
    assert root.NodeValue == 0
    assert root.Parent is None
    assert len(root.Children) == 1
    assert root.Children[0] is node_2
    assert node_2.NodeValue == 2
    assert node_2.Parent is root
    assert node_2.Children == []

    tree.DeleteNode(node_2)
    assert tree.Root is root
    assert root.NodeValue == 0
    assert root.Parent is None
    assert root.Children == []

def test_get_all_nodes(setup_three_leaf):
    tree, root = setup_three_leaf
    node_1, node_2 = root.Children
    node_3 = node_1.Children[0]
    nodes = tree.GetAllNodes()
    assert len(nodes) == 4
    assert root in nodes
    assert node_1 in nodes
    assert node_2 in nodes
    assert node_3 in nodes
    empty_tree = SimpleTree(None)
    assert empty_tree.GetAllNodes() == []

def test_find_nodes_by_value(setup_three_leaf):
    tree, root = setup_three_leaf
    node_1, node_2 = root.Children
    node_3 = node_1.Children[0]
    node_4 = SimpleTreeNode(2, None)
    tree.AddChild(node_3, node_4)
    nodes = tree.FindNodesByValue(0)
    assert len(nodes) == 1
    assert root in nodes
    nodes = tree.FindNodesByValue(1)
    assert len(nodes) == 1
    assert node_1 in nodes
    nodes = tree.FindNodesByValue(2)
    assert len(nodes) ==2
    assert node_2 in nodes
    assert node_4 in nodes
    nodes = tree.FindNodesByValue(3)
    assert len(nodes) == 1
    assert node_3 in nodes
    assert tree.FindNodesByValue(5) == []
    empty_tree = SimpleTree(None)
    assert empty_tree.FindNodesByValue(1) == []

def test_move_node(setup_three_leaf):
    tree, root = setup_three_leaf
    node_1, node_2 = root.Children
    node_3 = node_1.Children[0]
    node_4 = SimpleTreeNode(4, None)
    tree.AddChild(node_3, node_4)    
    tree.MoveNode(node_3, node_2)
    assert tree.Root is root
    assert root.NodeValue == 0
    assert root.Parent is None
    assert len(root.Children) == 2
    assert root.Children[0] is node_1
    assert root.Children[1] is node_2
    assert node_2.NodeValue == 2
    assert node_2.Parent is root
    assert len(node_2.Children) == 1
    assert node_2.Children[0] is node_3
    assert node_1.NodeValue == 1
    assert node_1.Parent is root
    assert node_1.Children == []
    assert node_3.NodeValue == 3
    assert node_3.Parent is node_2
    assert len(node_3.Children) == 1
    assert node_3.Children[0] == node_4
    assert node_4.NodeValue == 4
    assert node_4.Parent is node_3
    assert node_4.Children == []

def test_count(setup_only_root, setup_three_leaf):
    tree, _ = setup_only_root
    assert tree.Count() == 1
    tree, _ = setup_three_leaf
    assert tree.Count() == 4
    empty_tree = SimpleTree(None)
    assert empty_tree.Count() == 0

def test_leaf_count(setup_only_root, setup_three_leaf):
    tree, _ = setup_only_root
    assert tree.LeafCount() == 0
    tree, _ = setup_three_leaf
    assert tree.LeafCount() == 3
    empty_tree = SimpleTree(None)
    assert empty_tree.LeafCount() == 0

'''
Само дерево в простейшем виде (допустим, класс SimpleTree) реализуется также максимально просто: это в общем случае всего лишь корневой элемент дерева. То есть в классе SimpleTree достаточно завести только одно поле, root, хранящее либо корневой узел, либо отсутствие значения.

Какие операции в классе SimpleTree нам потребуются:
- добавить текущему узлу (первый параметр метода добавления узла) новый узел (второй параметр метода добавления узла) в качестве дочернего (тест: проверяем наличие добавленного узла);
- удалить некорневой узел (удаляется узел вместе со всем поддеревом) (тест: проверяем отсутствие удалённого узла и его потомков);
- последовательно обойти всё дерево и сформировать список всех узлов в произвольном порядке;
- найти список подходящих узлов по заданному значению (тест: проверяем результат с тестовым списком);
- переместить некорневой узел дочерним узлом в другое место дерева (вместе с его поддеревом), для чего воспользуйтесь предыдущими методами (тест: проверяем, что узел отсутствует там где был исходно и появился в новом месте);
- подсчитать общее количество узлов в дереве, и количество листьев (тест: проверяем на контрольном дереве количество узлов и листьев).

Также напишите метод, который перебирает всё дерево и прописывает каждому узлу его уровень.
Деревья очень "рекурсивны", наиболее удобно и правильно думать о них именно в парадигме рекурсивных вычислений [CS106B].

Придумайте, как лучше организовать поддержку уровня узлов без анализа всего дерева.
'''