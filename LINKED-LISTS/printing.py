class Singly_linked:
   def __init__(self,head):
       self.head=head

   def print_(self):
       print(f'The SLL values are as follows')
       node=self.head
       while node.next!=None:
           print(f'{node.info} \n')
           node = node.next
       print(f'{node.info} \n')
class Node_:
    def __init__(self,info):
        self.info = info
        self.next = None
n1 = Node_(1)

n2 = Node_(2)
n3 = Node_(3)

n1.next  = n2
n2.next  = n3

SLL = Singly_linked(n1)

SLL.print_()


