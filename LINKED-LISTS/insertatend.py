# Given the head of a singly linked list and a value, insert a new node with that value at the end of the list.

# Input:
# Initial list: 1 → 2 → 3, value = 4
# Output:
# 1 → 2 → 3 → 4

# class sll:
#     def __init__(self,head):
#         self.head = head
#
#     def print_(self):
#         curr = self.head
#         while curr:
#             print(f'Value = {curr.value}')
#             curr=curr.next

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_(self,head):
        curr = head
        while curr:
            print(f'Value = {curr.value}')
            curr=curr.next

def create_from_list(item):
    head =Node(item[0])
    # sll_ =sll(head)

    prev = head

    for i in range(1,len(item)):
        curr = Node(item[i])
        prev.next = curr
        prev=curr

    return head



head = create_from_list([1,2,3])

head.print_(head)
