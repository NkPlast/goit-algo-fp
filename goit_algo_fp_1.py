class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def merge_sort(self):
        def get_middle(node):
            if not node:
                return node
            slow = node
            fast = node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def sorted_merge(a, b):
            if not a:
                return b
            if not b:
                return a
            if a.data <= b.data:
                result = a
                result.next = sorted_merge(a.next, b)
            else:
                result = b
                result.next = sorted_merge(a, b.next)
            return result

        def merge_sort_recursive(node):
            if not node or not node.next:
                return node
            middle = get_middle(node)
            next_to_middle = middle.next
            middle.next = None
            left = merge_sort_recursive(node)
            right = merge_sort_recursive(next_to_middle)
            return sorted_merge(left, right)

        self.head = merge_sort_recursive(self.head)

    def merge_with(self, other_list):
        def merge_two_sorted_lists(l1, l2):
            dummy = Node(0)
            tail = dummy
            while l1 and l2:
                if l1.data < l2.data:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 or l2
            return dummy.next
        
        self.head = merge_two_sorted_lists(self.head, other_list.head)

# Тестування
list1 = LinkedList()
list2 = LinkedList()

for value in [7, 2, 4, 9, 1]:
    list1.append(value)
for value in [6, 5, 3, 8]:
    list2.append(value)

print("Original List 1:")
list1.print_list()
print("Original List 2:")
list2.print_list()

list1.reverse()
print("Reversed List 1:")
list1.print_list()

list1.merge_sort()
print("Sorted List 1:")
list1.print_list()

list2.merge_sort()
print("Sorted List 2:")
list2.print_list()

list1.merge_with(list2)
print("Merged Sorted List:")
list1.print_list()
