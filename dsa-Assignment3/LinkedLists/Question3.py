class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def remove_node(head, node):
    if not head or not node:
        return head

   
    if node == head:
        head = head.next
        if head:
            head.prev = None
        return head

   
    if node.prev:
        node.prev.next = node.next
    if node.next:
        node.next.prev = node.prev

    return head

def print_doubly_list(head):
    current = head
    while current:
        print(current.data, end=" ⇔ ")
        current = current.next
    print("None")


head = DoublyNode(1)
node2 = DoublyNode(2)
node3 = DoublyNode(3)
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2

print("Original Doubly Linked List:")
print_doubly_list(head)
head = remove_node(head, node2)
print("After removing node with value 2:")
print_doubly_list(head)
