"""Implementation of a Binary Search Tree"""

from collections import deque  


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

    def dfs_traverse(self, func, method):
        """Perform a DFS tree traversal, employing a specific traversal method and executing a function for each visited Node's data."""
        if method == 'pre-order':
            self._recursively_dfs_traverse_pre_order(func, self.root)

        elif method == 'in-order':
            self._recursively_dfs_traverse_in_order(func, self.root)

        elif method == 'reverse-in-order':
            self._recursively_dfs_traverse_reverse_in_order(func, self.root)

        elif method == 'post-order':
            self._recursively_dfs_traverse_post_order(func, self.root)

        else:
            raise ValueError(f"Invalid DFS traversal method: {method}")

    def _recursively_dfs_traverse_pre_order(self, func, node):
        """Recursively perform pre-order DFS traversal, executing a function on each visited Node's data."""
        if node is None:
            return

        # Handle current Node
        func(node.data)
        
        # Traverse the left subtree
        self._recursively_dfs_traverse_pre_order(func, node.left)
        
        # Traverse the right subtreee
        self._recursively_dfs_traverse_pre_order(func, node.right)

    def _recursively_dfs_traverse_in_order(self, func, node):
        """Recursively perform in-order DFS traversal, executing a function on each visited Node's data."""
        if node is None:
            return
        
        # Traverse the left subtree
        self._recursively_dfs_traverse_in_order(func, node.left)
        
        # Handle current Node
        func(node.data)

        # Traverse the right subtreee
        self._recursively_dfs_traverse_in_order(func, node.right)

    def _recursively_dfs_traverse_reverse_in_order(self, func, node):
        """Recursively perform reverse-in-order DFS traversal, executing a function on each visited Node's data."""
        if node is None:
            return
        
        # Traverse the right subtreee
        self._recursively_dfs_traverse_reverse_in_order(func, node.right)

        # Handle current Node
        func(node.data)

        # Traverse the left subtree
        self._recursively_dfs_traverse_reverse_in_order(func, node.left)

    def _recursively_dfs_traverse_post_order(self, func, node):
        """Recursively perform post-order DFS traversal, executing a function on each visited Node's data."""
        if node is None:
            return
        
        # Traverse the left subtree
        self._recursively_dfs_traverse_post_order(func, node.left)
        
        # Traverse the right subtreee
        self._recursively_dfs_traverse_post_order(func, node.right)

        # Handle current Node
        func(node.data)

    def bfs_traverse(self, func):
        """Perform a BFS traversal of the tree, executing a function on each visited Node's data."""

        # Handle edge case where trying to traverse and empty tree
        if self.root is None:
            return

        queue = deque([self.root])

        while queue:

            node = queue.popleft()  
            
            # Execute the callback function on the Node's data
            func(node.data) 
            
            # Enqueue left child  
            if node.left is not None:  
                queue.append(node.left)  
    
            # Enqueue right child  
            if node.right is not None:  
                queue.append(node.right)  


# --- Execution --- #

bst = BinarySearchTree()

# insert_values = [5, 4, 6, 8, 3, 7]
insert_values = ['F', 'B', 'G', 'A', 'D', 'I', 'C', 'E', 'H']
for val in insert_values:
    bst.insert(val)

# bst.dfs_traverse(print, method='post-order')
bst.bfs_traverse(print)

