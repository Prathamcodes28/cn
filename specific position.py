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

new_node=node(25)


# Traversing to find node with data 20
current = node1
while current is not None and current.data != 20:
    current = current.next

# Inserting new node after 20
if current is not None:  # Ensuring 20 exists in the list
    new_node.next = current.next
    current.next = new_node

# **Printing the linked list directly (Without function)**
current = node1
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")  # Indicates end of list
