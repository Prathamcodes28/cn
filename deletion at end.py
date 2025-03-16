class node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
head = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)

# Linking nodes
head.next = node2
node2.next = node3
node3.next = node4

# ✅ Deleting the node from the end without 'if-else'
current = head
if current is not None and current.next is not None:  # Ensures valid list
    while current.next.next is not None:
        current = current.next
    current.next = None
else:
    head = None  # Handles single-node or empty list cases

# Display the updated linked list
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
