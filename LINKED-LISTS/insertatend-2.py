# Given the head of a singly linked list and a value, insert a new node with that value at the end of the list.

# Input:
# Initial list: 1 → 2 → 3, value = 4
# Output:
# 1 → 2 → 3 → 4

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_(self,head):
        curr = head
        while curr:
            print(f'Value = {curr.value}')
            curr=curr.next

    def insert_end(self,head,value):
        curr = head
        while curr:
            if curr.next ==None:
                curr.next = Node(value)
                break
            curr = curr.next

def create_from_list(item):
    sll =Node(item[0])
    # sll_ =sll(head)

    prev = sll

    for i in range(1,len(item)):
        curr = Node(item[i])
        prev.next = curr
        prev=curr

    return sll



sll = create_from_list([1,2,3,4])

sll.print_(sll)

sll.insert_end(sll,5)
sll.print_(sll)