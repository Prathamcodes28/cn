class node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=node(10)
node2=node(20)
node3=node(30)
node4=node(40)

node1.next=node2
node2.next=node3
node3.next=node4

head=node1
new_node=node(50) # is ek node bani uske andaar data gya fir next step mein pointer value aayi
new_node.next=head # head ki value new node ki di jise new node add or pointer bhi mila because of .next ki karn ab 
head=new_node   #head ko update karna hai jo refernece address deta hai ko kaise bhul sakte hai fir new node ka address hai vo head lega

current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
