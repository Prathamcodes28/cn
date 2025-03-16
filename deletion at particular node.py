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

# Deleting node with data = 30
current = head

# Edge case: If the node to delete is the head itself
if current.data == 30:
    head = current.next
else:
    while current.next is not None:   # Traverse till we find the node
        if current.next.data == 30:
            current.next = current.next.next  # Delete the node
            break
        current = current.next

# Display the updated linked list
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
