class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder_dfs(root: TreeNode):
    """Non-recursively conduct preorder depth first search."""

    visited = set()  # Keep track of visited nodes
    stack = [root]   # Implement a stack data structure as a list from which we'll append/pop TreeNodes as we search the tree

    while stack:
        
        # Pop a node off the stack
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)

            # Do something with the node data
            print(node.data)

            # Add right child to the stack (if it exists)
            if node.right:
                stack.append(node.right)

            # Add left child to the stack (if it exists). Thus, we'll search the tree from left to right.
            if node.left:
                stack.append(node.left)


def recursive_preorder_dfs(root: TreeNode):
    """Recursively conduct preorder depth first search."""
    
    if root:
    
        # First print the data of node
        print(root.data)
  
        # Then recursively search the left child tree
        recursive_preorder_dfs(root.left)
  
        # Then recursively search the right child tree
        recursive_preorder_dfs(root.right)


# ----- Execution ----- #

# --- Tree Setup --- #

# Leaf nodes (with no children)
node_7 = TreeNode(7)
node_6 = TreeNode(6)
node_5 = TreeNode(5)
node_4 = TreeNode(4)

# Middle nodes
node_3 = TreeNode(3, node_6, node_7)
node_2 = TreeNode(2, node_4, node_5)

# Root node
node_1 = TreeNode(1, node_2, node_3)

# --- DFS --- #
preorder_dfs(node_1)
print()
recursive_preorder_dfs(node_1)
