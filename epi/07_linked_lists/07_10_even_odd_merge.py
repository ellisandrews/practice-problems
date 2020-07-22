"""
Consider a singly linked list whose nodes are numbered starting at 0.
Define the even-odd merge of the list to be the list consisting of the even-numbered nodes followed by the odd-numbered nodes.
Write a program that computes the even-odd merge.


Example:

Input: L0 -> L1 -> L2 -> L3 -> L4
Output: L0 -> L2 -> L4 -> L1 -> L3
"""

# Define objects

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_
        nodes.append('None')
        return ' -> '.join(nodes)


class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next_ = next_


# Make input linked list
l4 = Node(4)
l3 = Node(3, next_=l4)
l2 = Node(2, next_=l3)
l1 = Node(1, next_=l2)
l0 = Node(0, next_=l1)

input_llist = LinkedList(head=l0)


def even_odd_merge(llist):
    return llist


print(even_odd_merge(input_llist))

# assert even_odd_merge(llist).__repr__() == '0 -> 2 -> 4 -> 1 -> 3 -> None'
