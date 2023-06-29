import pytest
from simple_tree import SimpleTreeNode, SimpleTree

@pytest.fixture
def setup():
    root = SimpleTreeNode(0, None)
    tree = SimpleTree(root)
    return tree, root

def test_init(setup):    
    tree, root = setup
    assert tree.Root is root
    assert root.NodeValue == 0
    assert root.Parent is None
    assert root.Children == []
    empty_tree = SimpleTree(None)
    assert empty_tree.Root is None

def test_add_child(setup):
    tree, root = setup
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

def test_delete_node(setup):
    tree, root = setup
    node_1 = SimpleTreeNode(1, None)
    tree.AddChild(root, node_1)
    node_2 = SimpleTreeNode(2, None)
    tree.AddChild(root, node_2)
    node_3 = SimpleTreeNode(3, None)
    tree.AddChild(node_1, node_3)
    
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