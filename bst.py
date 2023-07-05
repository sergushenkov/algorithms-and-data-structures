class BSTNode:

    def __init__(self, key, val, parent=None):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо добавить новый узел левым потомком


class BST:

    def __init__(self, node=None):
        self.Root = node  # корень дерева или None

    def FindNodeByKey(self, key):
        found = BSTFind()
        next_node = self.Root
        found.Node = next_node
        while next_node is not None and next_node.NodeKey != key:
            if key < next_node.NodeKey:
                next_node = next_node.LeftChild
                found.ToLeft = True
            else:
                next_node = next_node.RightChild
                found.ToLeft = False
            if next_node is not None:
                found.Node = next_node
        if next_node is None:
            return found
        found.NodeHasKey = True
        return found

    def AddKeyValue(self, key, val):
        found_node = self.FindNodeByKey(key)
        if found_node.NodeHasKey is True:
            return False
        new_node = BSTNode(key, val, found_node.Node)
        if found_node.ToLeft:
            found_node.Node.LeftChild = new_node
        else:
            found_node.Node.RightChild = new_node
        return True

    def FinMinMax(self, FromNode, FindMax):
        if self.Root is None or FromNode is None:
            return None
        found_node = FromNode
        if FindMax:
            next_node = FromNode.RightChild
        else:
            next_node = FromNode.LeftChild
        while next_node is not None:
            found_node = next_node
            if FindMax:
                next_node = next_node.RightChild
            else:
                next_node = next_node.LeftChild
        return found_node

    def DeleteNodeByKey(self, key):
        for_delete = self.FindNodeByKey(key)
        if for_delete.NodeHasKey is False:
            return False

        if for_delete.Node is self.Root:
            self.Root = None
            return True

        if for_delete.Node.LeftChild is None and for_delete.Node.RightChild is None:
            parent_node = for_delete.Node.Parent
            if parent_node.LeftChild is for_delete.Node:
                parent_node.LeftChild = None
            else:
                parent_node.RightChild = None
            return True

        if for_delete.Node.LeftChild is None or for_delete.Node.RightChild is None:
            if for_delete.Node.LeftChild is None:
                child_node = for_delete.Node.RightChild
            else:
                child_node = for_delete.Node.LeftChild
            parent_node = for_delete.Node.Parent
            child_node.Parent = parent_node
            if parent_node.LeftChild is for_delete.Node:
                parent_node.LeftChild = child_node
            else:
                parent_node.RightChild = child_node
            return True

        change_node = self.FinMinMax(for_delete.Node.RightChild, FindMax=False)
        if change_node is not for_delete.Node.RightChild:
            change_node.Parent.LeftChild = change_node.RightChild  # is None or node
        change_node.LeftChild = for_delete.Node.LeftChild
        change_node.LeftChild.Parent = change_node
        if for_delete.Node.Parent.LeftChild is for_delete.Node:
            for_delete.Node.Parent.LeftChild = change_node
        else:
            for_delete.Node.Parent.RightChild = change_node
        change_node.Parent = for_delete.Node.Parent
        return True

    def Count(self):
        if self.Root is None:
            return 0
        node_count = 1
        nodes = [self.Root.LeftChild, self.Root.RightChild]
        while nodes:
            node = nodes.pop()
            if node is None:
                continue
            node_count += 1
            nodes.extend([node.LeftChild, node.RightChild])
        return node_count
