import gvgen

graph = gvgen.GvGen()


class Node:
    def __init__(self, val):
        self.parent = None
        self.left = None
        self.middle = None
        self.right = None
        self.val = val
        self.visited = False


    def __str__(self):
        return "{}".format(int(self.val))

def add_left(current, parent_node):
    current.left = Node(4 + current.val)
    current.left.parent = current
    left_node = graph.newItem(current.left)
    link_left = graph.newLink(parent_node, left_node)
    graph.propertyAppend(link_left, "label", 4)
    add(current.left, left_node)


def add_mid(current, parent_node):
    current.middle = Node(5 + current.val)
    current.middle.parent = current
    middle_node = graph.newItem(current.middle)
    link_middle = graph.newLink(parent_node, middle_node)
    graph.propertyAppend(link_middle, "label", 5)
    add(current.middle, middle_node)


def add_right(current, parent_node):
    current.right = Node(6 + current.val)
    current.right.parent = current
    right_node = graph.newItem(current.right)
    link_right = graph.newLink(parent_node, right_node)
    graph.propertyAppend(link_right, "label", 6)
    add(current.right, right_node)



def add(current, parent_node):
    if current.val < 21:
        if current.left is None:
            add_left(current, parent_node)
            add_mid(current, parent_node)
            add_right(current, parent_node)




root = Node(0)
parent_zero = graph.newItem(root.val)
add(root, parent_zero)
