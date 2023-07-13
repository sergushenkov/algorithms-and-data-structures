from bbst import BSTNode, BalancedBST


def test_generate_tree():

    # empty tree
    tree = BalancedBST()
    array = ()
    tree.GenerateTree(array)
    assert tree.Root is None

    # only root
    tree = BalancedBST()
    array = (1,)
    tree.GenerateTree(array)
    assert tree.Root.NodeKey == 1
    assert tree.Root.Parent is None
    assert tree.Root.LeftChild is None
    assert tree.Root.RightChild is None
    assert tree.Root.Level == 0

    # three nodes
    tree = BalancedBST()
    array = (1, 2, 3)
    tree.GenerateTree(array)
    assert tree.Root.NodeKey == 2
    assert tree.Root.Parent is None
    assert tree.Root.Level == 0
    assert tree.Root.LeftChild.NodeKey == 1
    assert tree.Root.LeftChild.Parent is tree.Root
    assert tree.Root.LeftChild.LeftChild is None
    assert tree.Root.LeftChild.RightChild is None
    assert tree.Root.LeftChild.Level == 1
    assert tree.Root.RightChild.NodeKey == 3
    assert tree.Root.RightChild.Parent is tree.Root
    assert tree.Root.RightChild.LeftChild is None
    assert tree.Root.RightChild.RightChild is None
    assert tree.Root.RightChild.Level == 1

    # six nodes
    tree = BalancedBST()
    array = (1, 2, 3, 4, 5, 6)
    tree.GenerateTree(array)
    assert tree.Root.NodeKey == 3
    assert tree.Root.Parent is None
    assert tree.Root.Level == 0
    assert tree.Root.LeftChild.NodeKey == 1
    assert tree.Root.LeftChild.Parent is tree.Root
    assert tree.Root.LeftChild.LeftChild is None
    assert tree.Root.LeftChild.Level == 1
    assert tree.Root.LeftChild.RightChild.NodeKey == 2
    assert tree.Root.LeftChild.RightChild.Parent is tree.Root.LeftChild
    assert tree.Root.LeftChild.RightChild.LeftChild is None
    assert tree.Root.LeftChild.RightChild.RightChild is None
    assert tree.Root.LeftChild.RightChild.Level == 2
    assert tree.Root.RightChild.NodeKey == 5
    assert tree.Root.RightChild.Parent is tree.Root
    assert tree.Root.RightChild.Level == 1
    assert tree.Root.RightChild.LeftChild.NodeKey == 4
    assert tree.Root.RightChild.LeftChild.Parent is tree.Root.RightChild
    assert tree.Root.RightChild.LeftChild.LeftChild is None
    assert tree.Root.RightChild.LeftChild.RightChild is None
    assert tree.Root.RightChild.LeftChild.Level == 2
    assert tree.Root.RightChild.RightChild.NodeKey == 6
    assert tree.Root.RightChild.RightChild.Parent is tree.Root.RightChild
    assert tree.Root.RightChild.RightChild.LeftChild is None
    assert tree.Root.RightChild.RightChild.RightChild is None
    assert tree.Root.RightChild.RightChild.Level == 2


def test_is_balansed():
    # empty tree
    tree = BalancedBST()
    array = ()
    tree.GenerateTree(array)
    assert tree.IsBalanced(tree.Root) is True

    # only root
    tree = BalancedBST()
    array = (1,)
    tree.GenerateTree(array)
    assert tree.IsBalanced(tree.Root) is True

    # three nodes
    tree = BalancedBST()
    array = (1, 2, 3)
    tree.GenerateTree(array)
    assert tree.IsBalanced(tree.Root) is True
    node_4 = BSTNode(4, tree.Root.RightChild)
    node_4.Level = tree.Root.RightChild.Level + 1
    tree.Root.RightChild.RightChild = node_4
    assert tree.IsBalanced(tree.Root) is True
    node_5 = BSTNode(5, node_4.RightChild)
    node_4.RightChild = node_5
    node_5.Level = node_4.Level + 1
    assert tree.IsBalanced(tree.Root) is False
    tree.Root.RightChild.RightChild = None
    assert tree.IsBalanced(tree.Root) is True
