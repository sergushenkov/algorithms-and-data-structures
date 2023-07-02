class SimpleTreeNode:
    def __init__(self, val, parent=None):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:
    def __init__(self, root=None):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        if self.Root is None:
            return []
        nodes = [self.Root]
        for node in self.Root.Children:
            child_tree = SimpleTree(node)
            nodes.extend(child_tree.GetAllNodes())
        return nodes

    def FindNodesByValue(self, val):
        nodes = []
        for node in self.GetAllNodes():
            if node.NodeValue == val:
                nodes.append(node)
        return nodes

    def MoveNode(self, OriginalNode, NewParent):
        old_parent = OriginalNode.Parent
        old_parent.Children.remove(OriginalNode)
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        node_count = 0
        for node in self.GetAllNodes():
            if node.Children == []:
                node_count += 1
        return node_count
