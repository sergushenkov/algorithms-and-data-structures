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

    def EvenTrees(self):
        need_to_cut = []
        all_nodes = self.GetAllNodes()
        cuted_nodes = set()
        node_cost = dict()
        while len(all_nodes) > 2:
            for node in all_nodes:
                if node in node_cost:
                    continue
                is_early = False
                is_leaf = True
                cnt_nodes = 1
                for child in node.Children:
                    if child not in node_cost:
                        is_early = True
                        break
                    if child not in cuted_nodes:
                        is_leaf = False
                        cnt_nodes += node_cost[child]
                if is_early:
                    continue
                if is_leaf:
                    node_cost[node] = 1
                    continue
                node_cost[node] = cnt_nodes
                if node.Parent is not None and cnt_nodes % 2 == 0:
                    need_to_cut.extend([node.Parent, node])
                if cnt_nodes % 2 == 0:
                    node_in_cuting = [node]
                    while node_in_cuting:
                        cut_node = node_in_cuting.pop()
                        node_in_cuting.extend(cut_node.Children)
                        cuted_nodes.add(cut_node)
                        if cut_node in all_nodes:
                            all_nodes.remove(cut_node)
                    break
        return need_to_cut
