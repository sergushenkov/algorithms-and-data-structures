'''
. Проблема в том, что нельзя просто взять и заменить узел одним его потомком, потому что тут возможны конфликтные ситуации, связанные с упорядоченностью ключей. Не будем углубляться в эту ситуацию, воспользуемся следующим правилом: удаляемый узел надо заменить так называемым узлом-преемником, ключ которого -- наименьший из всех ключей, которые больше ключа удаляемого узла.
Иными словами, нам надо взять правого потомка удаляемого узла, и далее спускаться по всем левым потомкам. Если мы находим лист, то его и надо поместить вместо удаляемого узла. Если мы находим узел, у которого есть только правый потомок, то преемником берём этот узел, а вместо него помещаем его правого потомка.
'''

class BSTNode:

    def __init__(self, key, val, parent=None):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если в дереве вообще нету узлов
        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо добавить новый узел левым потомком

class BST:

    def __init__(self, node=None):
        self.Root = node # корень дерева или None

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
        found = self.FindNodeByKey(key)
        if found.NodeHasKey is False:
            return False
        if found.Node is self.Root:
            
        # if found.Node.LeftChild is None and found.Node.RightChild is None:
        #     parent_node = found.Node.Parent
        #     if parent_node 
        # return True
        

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