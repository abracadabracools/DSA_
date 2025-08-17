# Problem 3: Delete a Node by Value
# 📝 Problem Statement
# Given the head of a singly linked list and a target value, delete the first node that contains this value. Return the new head of the linked list.
#
# 📌 Example
# Input:
# List = 1 → 2 → 3 → 4, value = 3
# Output:
# 1 → 2 → 4


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_(head):
    curr = head
    while curr:
        print(f'Value = {curr.value}')
        curr=curr.next

def insert_end(head,value):
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

def removebyvalue(head,val):
    if head.value == val:
        return head.next
    prev=head
    curr=head.next
    while curr:
        if curr.value == val:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next
    return head


sll = create_from_list([1,2,3,4])
print_(sll)
print('\n')
sll = removebyvalue(sll,1)
print_(sll)