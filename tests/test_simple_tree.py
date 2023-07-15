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
    assert len(nodes) == 2
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
    assert tree.LeafCount() == 1
    tree, _ = setup_three_leaf
    assert tree.LeafCount() == 2
    empty_tree = SimpleTree(None)
    assert empty_tree.LeafCount() == 0


def nodes2values(nodes):
    values = []
    for node in nodes:
        values.append(node.NodeValue)
    return values


def test_even_trees(setup_only_root, setup_three_leaf):
    empty_tree = SimpleTree(None)
    assert empty_tree.EvenTrees() == []
    tree, _ = setup_only_root
    assert tree.EvenTrees() == []

    tree, _ = setup_three_leaf
    assert nodes2values(tree.EvenTrees()) == [0, 1]

    node_1 = SimpleTreeNode(1, None)
    tree = SimpleTree(node_1)
    node_2 = SimpleTreeNode(2, None)
    tree.AddChild(node_1, node_2)
    node_3 = SimpleTreeNode(3, None)
    tree.AddChild(node_1, node_3)
    node_6 = SimpleTreeNode(6, None)
    tree.AddChild(node_1, node_6)
    node_5 = SimpleTreeNode(5, None)
    tree.AddChild(node_2, node_5)
    node_7 = SimpleTreeNode(7, None)
    tree.AddChild(node_2, node_7)
    node_4 = SimpleTreeNode(4, None)
    tree.AddChild(node_3, node_4)
    node_8 = SimpleTreeNode(8, None)
    tree.AddChild(node_6, node_8)
    node_9 = SimpleTreeNode(9, None)
    tree.AddChild(node_8, node_9)
    node_10 = SimpleTreeNode(10, None)
    tree.AddChild(node_8, node_10)
    assert nodes2values(tree.EvenTrees()) == [1, 3, 1, 6]
