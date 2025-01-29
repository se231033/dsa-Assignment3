
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    new_head = None
    while head:
        new_node = Node(head.data)
        new_node.next = new_head
        new_head = new_node
        head = head.next
    return new_head

def print_list(head):
    current = head
    while current:
        print(current.data, end=" → ")
        current = current.next
    print("None")

# Test Case
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
print("Original List:")
print_list(head)
reversed_head = reverse(head)
print("Reversed List:")
print_list(reversed_head)
