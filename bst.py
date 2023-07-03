'''
.  метод поиска (тест: проверяем поиск отсутствующего ключа в двух вариантах (запрошенный ключ добавляем либо левому, либо правому потомку) и поиск присутствующего ключа);
.  метод добавления нового узла, задаём добавляемый ключ и соответствующее ему значение (тесты: проверяем исходное отсутствие узла по такому ключу в дереве и его наличие после добавления, в двух вариантах - левым или правым узлом родителя, а также попытку добавления ключа, которое уже имеется в дереве, в таком случае ничего с деревом не делаем);
.  поиск максимального и минимального ключей, начиная с заданного узла (тест, 4 варианта: поиск начиная с корня и поиск начиная с поддерева, ищем максимальный и минимальный ключ);
.  метод удаления узла по его ключу (тест: проверяем исходное наличие узла у родителя, его отсутствие после удаления, и результат работы метода).
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
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        found_node = BSTFind()
        next_node = self.Root
        found_node.Node = next_node
        while next_node is not None and next_node.NodeKey != key:
            if key < next_node.NodeKey:
                next_node = next_node.LeftChild
                found_node.ToLeft = True
            else:
                next_node = next_node.RightChild
                found_node.ToLeft = False
            if next_node is not None:
                found_node.Node = next_node
        if next_node is None:
            return found_node
        found_node.NodeHasKey = True
        return found_node

    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        return False # если ключ уже есть
  
    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        return None

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        return False # если узел не найден

    def Count(self):
        return 0 # количество узлов в дереве