# list1: 1 → 2 → 4
# list2: 1 → 3 → 4
#
# Output:
# 1 → 1 → 2 → 3 → 4 → 4


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_(head):
    curr = head
    while curr:
        print(f'Value = {curr.value}')
        curr=curr.next
    print('\n')

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

def merge_(l1,l2):
    curr1=l1
    curr2=l2

    head = None
    while curr1 and curr2:
        if curr1.value <= curr2.value:
            trace = curr1.next
            curr1.next = curr2
            curr1 =trace
            curr2 =curr2.next
        else:
            trace = curr2.next
            curr2.next = curr1
            curr2 = trace
            curr1 = curr1.next
    return curr1

curr1 = create_from_list([0,2,5])
print_(curr1)
curr2 = create_from_list([1,3,4])
print_(curr2)

print_(merge_(curr1,curr2))
