# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    # Insert a new node at the end
    # Time: O(n), space: O(1)
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Insert a new node at the beginning
    # Time: O(1), space: O(1)
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Print the linked list
    # Time: O(n), space: O(1)
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Delete first occurrence of a value
    # Time: O(n), space: O(1)
    def delete(self, key):
        current = self.head

        # If head needs to be deleted
        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current:  # Key found
            prev.next = current.next

    # Search for a value
    # Time: O(n), space: O(1)
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
ll.print_list()   # Output: 5 -> 10 -> 20 -> None

print(ll.search(10))  # True
ll.delete(10)
ll.print_list()       # Output: 5 -> 20 -> None