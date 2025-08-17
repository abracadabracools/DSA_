

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



sll = create_from_list([1,2,3,4])
print_(sll)