# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    if root is None:
        return None  

    max_value = root.value  

    left_max = greatest_node(root.left_child)
    right_max = greatest_node(root.right_child)

    if left_max is not None:
        max_value = max(max_value, left_max)
    if right_max is not None:
        max_value = max(max_value, right_max)

    return max_value
