class node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
node1 = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4

# New node to be added at the end
new_node = node(50)

# Traversing to the last node
head = node1
current = head

while current.next is not None:
    current = current.next

# Adding new_node at the end
current.next = new_node


# Printing the linked list
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
