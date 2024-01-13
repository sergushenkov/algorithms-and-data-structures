import pytest
from simple_tree_1 import SimpleTreeNode, SimpleTree


@pytest.fixture
def setup_only_root():
    root = SimpleTreeNode(0)
    tree = SimpleTree(root)
    return tree, root


@pytest.fixture
def setup_three_leaf(setup_only_root):
    root = SimpleTreeNode(0)
    tree = SimpleTree(root)
    node_1 = SimpleTreeNode(1)
    tree.add_child(root, node_1)
    node_2 = SimpleTreeNode(2)
    tree.add_child(root, node_2)
    node_3 = SimpleTreeNode(3)
    tree.add_child(node_1, node_3)
    return tree, root, node_1, node_2, node_3


def test_init(setup_only_root):
    tree = SimpleTree()
    assert tree.root is None

    tree, root = setup_only_root
    assert tree.root is root
    assert root.value == 0
    assert root.parent is None
    assert root.children == []


def test_add_child(setup_only_root):
    tree, root = setup_only_root
    child = SimpleTreeNode(1)
    tree.add_child(root, child)
    assert root.children == [child]

    assert child.parent is root


def test_delete_node(setup_three_leaf):
    tree, root, node_1, node_2, node_3 = setup_three_leaf
    assert node_2 in root.children
    assert node_2.parent is root

    tree.delete_node(node_2)
    assert root.children == [node_1]
    assert node_2.parent is None

    tree.delete_node(node_1)
    assert root.children == []


def test_get_all_nodes(setup_only_root, setup_three_leaf):
    tree = SimpleTree()
    all_nodes = tree.get_all_nodes()
    assert all_nodes == []

    tree, root = setup_only_root
    all_nodes = tree.get_all_nodes()
    assert all_nodes == [root]

    tree, root, node_1, node_2, node_3 = setup_three_leaf
    all_nodes = tree.get_all_nodes()
    assert all_nodes == [root, node_1, node_2, node_3]


def test_find_nodes_by_value(setup_three_leaf):
    tree = SimpleTree()
    nodes_with_2 = tree.find_nodes_by_value(2)
    assert nodes_with_2 == []

    tree, root, node_1, node_2, node_3 = setup_three_leaf
    nodes_with_2 = tree.find_nodes_by_value(2)
    assert nodes_with_2 == [node_2]

    node_3.value = 2
    nodes_with_2 = tree.find_nodes_by_value(2)
    assert nodes_with_2 == [node_2, node_3]
    nodes_with_3 = tree.find_nodes_by_value(3)
    assert nodes_with_3 == []


def test_move_node(setup_three_leaf):
    tree, root, node_1, node_2, node_3 = setup_three_leaf
    tree.move_node(node_1, node_2)
    assert node_1 not in root.children

    all_nodes = tree.get_all_nodes()
    assert all_nodes == [root, node_2, node_1, node_3]
    assert node_2.children == [node_1]

    assert node_1.parent is node_2
    assert node_1.children == [node_3]
    assert node_3.parent is node_1


def test_count(setup_three_leaf):
    tree = SimpleTree()
    cnt = tree.count()
    assert cnt == 0

    tree, root, node_1, node_2, node_3 = setup_three_leaf
    cnt = tree.count()
    assert cnt == 4
    tree.move_node(node_1, node_2)
    cnt = tree.count()
    assert cnt == 4


def test_leaf_count(setup_only_root, setup_three_leaf):
    tree = SimpleTree()
    cnt = tree.leaf_count()
    assert cnt == 0

    tree, root = setup_only_root
    cnt = tree.leaf_count()
    assert cnt == 1
    tree, root, node_1, node_2, node_3 = setup_three_leaf
    cnt = tree.leaf_count()
    assert cnt == 2
    tree.move_node(node_1, node_2)
    cnt = tree.leaf_count()
    assert cnt == 1
