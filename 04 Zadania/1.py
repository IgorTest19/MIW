import gvgen

graph = gvgen.GvGen()


class Node:
    def __init__(self, val):
        self.parent = None
        self.left = None
        self.middle = None
        self.right = None
        self.val = val



    def __str__(self):
        return "{}".format(int(self.val))

def add_left(current, parent_node, user):
    if user == "prot: ":
        user = "ant: "
    else:
        user = "prot: "
    current.left = Node(4 + current.val)
    current.left.parent = current
    left_node = graph.newItem(user + str(current.left))
    link_left = graph.newLink(parent_node, left_node)
    graph.propertyAppend(link_left, "label", 4)
    add(current.left, left_node, user)


def add_mid(current, parent_node, user):
    if user == "prot: ":
        user = "ant: "
    else:
        user = "prot: "
    current.middle = Node(5 + current.val)
    current.middle.parent = current
    middle_node = graph.newItem(user + str(current.middle))
    link_middle = graph.newLink(parent_node, middle_node)
    graph.propertyAppend(link_middle, "label", 5)
    add(current.middle, middle_node, user)


def add_right(current, parent_node, user):
    if user == "prot: ":
        user = "ant: "
    else:
        user = "prot: "
    current.right = Node(6 + current.val)
    current.right.parent = current
    right_node = graph.newItem(user + str(current.right))
    link_right = graph.newLink(parent_node, right_node)
    graph.propertyAppend(link_right, "label", 6)
    add(current.right, right_node, user)



def add(current, parent_node, user):
    if current.val < 21:
        if current.left is None:
            add_left(current, parent_node, user)
            add_mid(current, parent_node, user)
            add_right(current, parent_node, user)




root = Node(0)
user = "prot: "
parent_zero = graph.newItem(user + str(root.val))
add(root, parent_zero, user)

graph.dot()
