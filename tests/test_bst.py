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

def test_add_key_value(setup_only_root):
    tree, root = setup_only_root
    assert tree.AddKeyValue(10, 'J') is True
    assert root.RightChild is not None
    assert root.RightChild.NodeKey == 10
    assert root.RightChild.NodeValue == 'J'
    assert tree.AddKeyValue(10, 'J') is False
    assert tree.AddKeyValue(10, 'j') is False
    assert tree.AddKeyValue(-10, 'j') is True
    assert root.LeftChild is not None
    assert root.LeftChild.NodeKey == -10
    assert root.LeftChild.NodeValue == 'j'
    assert tree.AddKeyValue(5, 'E') is True
    assert tree.AddKeyValue(15, 'O') is True
    assert root.NodeKey == 0
    assert root.NodeValue == 'A'
    assert root.Parent is None
    assert root.LeftChild.NodeKey == -10
    assert root.LeftChild.NodeValue == 'j'
    assert root.LeftChild.Parent is root
    assert root.LeftChild.LeftChild is None
    assert root.LeftChild.RightChild is None
    assert root.RightChild.NodeKey == 10
    assert root.RightChild.NodeValue == 'J'
    assert root.RightChild.Parent is root
    assert root.RightChild.LeftChild.NodeKey == 5
    assert root.RightChild.LeftChild.NodeValue == 'E'
    assert root.RightChild.LeftChild.Parent is root.RightChild
    assert root.RightChild.LeftChild.LeftChild is None
    assert root.RightChild.LeftChild.RightChild is None
    assert root.RightChild.RightChild.NodeKey == 15
    assert root.RightChild.RightChild.NodeValue == 'O'
    assert root.RightChild.RightChild.Parent is root.RightChild
    assert root.RightChild.RightChild.LeftChild is None
    assert root.RightChild.RightChild.RightChild is None    

def test_find_min_max(setup_one_leaf):
    tree, root = setup_one_leaf
    tree.AddKeyValue(5, 'E')
    tree.AddKeyValue(15, 'O')
    tree.AddKeyValue(7, 'G')
    tree.AddKeyValue(12, 'M')
    max_node = tree.FinMinMax(root, True)
    assert max_node.NodeKey == 15
    assert max_node is tree.Root.RightChild.RightChild
    min_node = tree.FinMinMax(root, False)
    assert min_node.NodeKey == 0
    assert tree.FinMinMax(root.LeftChild, False) is None
    tree.AddKeyValue(-10, 'j')
    min_node = tree.FinMinMax(root.LeftChild, False)
    assert min_node.NodeKey == -10
    min_node = tree.FinMinMax(root, False)
    assert min_node.NodeKey == -10
    min_node = tree.FinMinMax(min_node, False)
    assert min_node.NodeKey == -10
    max_node = tree.FinMinMax(min_node, False)
    assert max_node.NodeKey == -10

    empty_tree = BST()
    assert empty_tree.FinMinMax(root, True) is None
    assert empty_tree.FinMinMax(root, False) is None

def test_delete_node_by_key(setup_one_leaf):
    tree, _ = setup_one_leaf
    tree.AddKeyValue(-10, 'j')
    tree.AddKeyValue(5, 'E')
    tree.AddKeyValue(15, 'O')
    tree.AddKeyValue(7, 'G')
    tree.AddKeyValue(8, 'H')
    assert tree.DeleteNodeByKey(-11) is False
    assert tree.Count() == 7
    assert tree.DeleteNodeByKey(-10) is True
    assert tree.Count() == 6
    assert tree.Root.LeftChild is None
    assert tree.FindNodeByKey(-10).NodeHasKey is False
    tree.DeleteNodeByKey(5)
    assert tree.Count() == 5
    assert tree.Root.LeftChild is None
    assert tree.FindNodeByKey(-10).NodeHasKey is False

def test_count(setup_only_root):
    empty_tree = BST()
    assert empty_tree.Count() == 0

    tree, _ = setup_only_root
    assert tree.Count() == 1
    tree.AddKeyValue(10, 'J')
    assert tree.Count() == 2
    tree.AddKeyValue(5, 'E')
    assert tree.Count() == 3
    tree.AddKeyValue(15, 'O')
    assert tree.Count() == 4
    tree.AddKeyValue(7, 'G')
    assert tree.Count() == 5
    tree.AddKeyValue(12, 'M')
    assert tree.Count() == 6