class BSTNode:

    def __init__(self, key, parent=None):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, array):
        if not array:
            return
        if len(array) == 1:
            node = BSTNode(array[0])
            self.Root = node
            return
        array = sorted(array)
        middle = (len(array) - 1) // 2
        node = BSTNode(array[middle])
        self.Root = node
        left_tree = BalancedBST()
        left_tree.GenerateTree(array[:middle])
        if left_tree.Root is not None:
            assert left_tree.Root.NodeKey < node.NodeKey
            self.Root.LeftChild = left_tree.Root
            self.Root.LeftChild.Parent = self.Root
        right_tree = BalancedBST()
        right_tree.GenerateTree(array[middle + 1:])
        if right_tree.Root is not None:
            assert right_tree.Root.NodeKey > node.NodeKey
            self.Root.RightChild = right_tree.Root
            self.Root.RightChild.Parent = self.Root

        nodes = [self.Root]
        while nodes:
            node = nodes.pop()
            if node is None:
                continue
            nodes.extend([node.LeftChild, node.RightChild])
            if node.Parent is None:
                continue
            node.Level = node.Parent.Level + 1

    def IsBalanced(self, root_node):
        if root_node is None:
            return True
        nodes = [root_node]
        levels = set()
        while nodes:
            node = nodes.pop()
            if node.LeftChild is None or node.RightChild is None:
                levels.add(node.Level)
            if node.LeftChild is not None:
                nodes.append(node.LeftChild)
            if node.RightChild is not None:
                nodes.append(node.RightChild)
        if not(levels) or max(levels) - min(levels) <= 1:
            return True
        return False
