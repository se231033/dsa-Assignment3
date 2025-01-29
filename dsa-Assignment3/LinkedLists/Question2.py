class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    current = head
    while current:
        print(current.data, end=" → ")
        current = current.next
    print("None")

def find_intersection(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 and list2:
        if list1.data == list2.data:
            current.next = Node(list1.data)
            current = current.next
            list1 = list1.next
            list2 = list2.next
        elif list1.data < list2.data:
            list1 = list1.next
        else:
            list2 = list2.next

    return dummy.next

# Test Case
list1 = Node(10)
list1.next = Node(20)
list1.next.next = Node(30)

list2 = Node(15)
list2.next = Node(20)
list2.next.next = Node(30)

print("Intersection List:")
intersection = find_intersection(list1, list2)
print_list(intersection)
