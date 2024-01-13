class SimpleTreeNode:
    def __init__(self, val):
        self.value = val  # значение в узле
        self.parent = None  # родитель или None для корня
        self.children = []  # список дочерних узлов


class SimpleTree:
    def __init__(self, root=None):
        self.root = root  # корень, может быть None

    def add_child(self, parent, child):
        parent.children.append(child)
        child.parent = parent

    def delete_node(self, node_to_delete):
        parent = node_to_delete.parent
        parent.children.remove(node_to_delete)
        node_to_delete.parent = None

    def get_all_nodes(self):
        if self.root is None:
            return []
        all_nodes = [self.root]
        i = 0
        while i < len(all_nodes):
            if len(all_nodes[i].children) > 0:
                all_nodes.extend(all_nodes[i].children)
            i += 1
        return all_nodes

    def find_nodes_by_value(self, val):
        if self.root is None:
            return []
        nodes = []
        all_nodes = [self.root]
        i = 0
        while i < len(all_nodes):
            if all_nodes[i].value == val:
                nodes.append(all_nodes[i])
            if len(all_nodes[i].children) > 0:
                all_nodes.extend(all_nodes[i].children)
            i += 1
        return nodes

    def move_node(self, node, new_parent):
        old_parent = node.parent
        old_parent.children.remove(node)
        new_parent.children.append(node)
        node.parent = new_parent

    def count(self):
        if self.root is None:
            return 0
        all_nodes = [self.root]
        i = 0
        while i < len(all_nodes):
            if len(all_nodes[i].children) > 0:
                all_nodes.extend(all_nodes[i].children)
            i += 1
        return len(all_nodes)

    def leaf_count(self):
        if self.root is None:
            return 0
        all_nodes = [self.root]
        leaf_count = 0
        i = 0
        while i < len(all_nodes):
            if len(all_nodes[i].children) == 0:
                leaf_count += 1
                i += 1
                continue
            all_nodes.extend(all_nodes[i].children)
            i += 1
        return leaf_count
