"""Implementation of a Binary Search Tree"""

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"< Node | data: {self.data} >"


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root  # Root Node

    def search(self, data):
        """Search for a piece of data (a Node) in the tree."""
        return self._recursively_search(data, self.root)

    def _recursively_search(self, data, node):
        """Recursively search the tree for a Node matching provided data."""
        # If we've exhausted tree or the Node has been found, return the result
        if node is None or node.data == data:
            return node

        # Continue searching the left subtree        
        if data < node.data:
            return self._recursively_search(data, node.left)
        
        # Continue searching the right subtree
        if data > node.data:
            return self._recursively_search(data, node.right)

    def insert(self, data):
        """Add a new piece of data (a new Node) to the tree"""
        # If there is no root node yet, make this node the root. Otherwise, begin insert process at the root.
        if not self.root:
            self.root = Node(data)
        else:
            self._recursively_insert(data, self.root)

    def _recursively_insert(self, data, node):
        """Recursively insert a new piece of data starting at a given Node."""
        # Continue insertion process on the left subtree
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._recursively_insert(data, node.left)
        
        # Continue insertion process on the right subtree
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._recursively_insert(data, node.right)
        
        # Don't allow duplicate data inserts
        else:
            raise ValueError(f"Cannot insert data: '{data}' as it already exists in the tree.")


# --- Execution --- #

bst = BinarySearchTree()

insert_values = [5, 4, 6, 8, 3, 7]
for val in insert_values:
    bst.insert(val)

print(bst.search(7))
print(bst.search(100))
