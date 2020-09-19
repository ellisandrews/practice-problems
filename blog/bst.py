"""Implementation of a Binary Search Tree"""

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        """Add a value to the tree"""
        # Create the new node to be inserted
        node = Node(value)
        
        # If there is no root node yet, make this node the root
        if not self.root:
            self.root = node
        else:
            self._recursively_insert(node, self.root)

    def _recursively_insert(self, new_node, current_node):
        """Recursively insert a new node by comparing to an existing node."""
        # Left
        if new_node.value < current_node.value:
            if not current_node.left:
                current_node.left = new_node
            else:
                self._recursively_insert(new_node, current_node.left)
        # Right
        elif new_node.value > current_node.value:
            if not current_node.right:
                current_node.right = new_node
            else:
                self._recursively_insert(new_node, current_node.right)
        # Equal
        else:
            raise ValueError(f"Cannot insert value: {new_node.value} as it already exists in the tree.")
        

# --- Execution --- #

bst = BinarySearchTree()

insert_values = [5, 4, 6, 8, 3, 7]
for val in insert_values:
    bst.insert(val)
