import pytest
from bst import BSTNode, BSTFind, BST


@pytest.fixture
def setup_only_root():
    root = BSTNode(0, 'A', None)
    tree = BST(root)
    return tree, root

@pytest.fixture
def setup_one_leaf():
    root = BSTNode(0, 'A', None)
    tree = BST(root)
    node_1 = BSTNode(10, 'J', root)
    root.RightChild = node_1
    return tree, root


def test_init(setup_only_root):
    tree, root = setup_only_root
    assert tree.Root == root
    assert root.NodeKey == 0
    assert root.NodeValue == 'A'
    assert root.Parent is None
    assert root.LeftChild is None
    assert root.RightChild is None

    empty_tree = BST()
    assert empty_tree.Root is None


def test_find_node_by_key(setup_one_leaf):
    tree, root = setup_one_leaf
    found_node = tree.FindNodeByKey(0)
    assert found_node.Node == root
    assert found_node.NodeHasKey is True
    assert found_node.ToLeft is False
    found_node = tree.FindNodeByKey(10)
    assert found_node.Node.NodeKey == root.RightChild.NodeKey
    assert found_node.Node == root.RightChild
    assert found_node.NodeHasKey is True
    assert found_node.ToLeft is False
    found_node = tree.FindNodeByKey(-10)
    assert found_node.Node == root
    assert found_node.NodeHasKey is False
    assert found_node.ToLeft is True
    found_node = tree.FindNodeByKey(7)
    assert found_node.Node == root.RightChild
    assert found_node.NodeHasKey is False
    assert found_node.ToLeft is True
    found_node = tree.FindNodeByKey(25)
    assert found_node.Node == root.RightChild
    assert found_node.NodeHasKey is False
    assert found_node.ToLeft is False

    empty_tree = BST()
    found_node = empty_tree.FindNodeByKey(25)
    assert found_node.Node is None
    assert found_node.NodeHasKey is False
    assert found_node.ToLeft is False
