class node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=node(10)
node2=node(20)
node3=node(30)
node4=node(40)

head.next=node2
node2.next=node3
node3.next=node4


#deleting the node from the begining

if head is not None:
    head=head.next #update the head to the next node


#printing the updated linked list

current=head
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")
