print("Code is like humor. When you have to explain it, it’s bad.")


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while (current.next):
            current = current.next
        current.next = newNode

    def insertBefore(self, needle, value):
        newNode = newNode = Node(value)

        if self.isEmpty():
            print('List is empty')
            return

        # if self.search(needle) is None:  + O(n)
        #     print('Needle not found')
        #     return

        # if self.length() == 1:           + O(n)
        #     newNode.next = self.head
        #     self.head = newNode
        #     return

        current = self.head
        prev = current
        while (current):
            if current.value == needle:
                prev.next = newNode
                newNode.next = current
                return

            prev = current
            current = current.next

        return True

    def delete(self, needle):
        if self.isEmpty():
            print('List is empty')
            return

        # if self.search(needle) is None: + O(n)
        #     print('Needle not found')
        #     return

        # Handle this with length property of class
        # if self.length() == 1:          + O(n) 
        #     self.head = None
        #     return

        current = self.head
        prev = current
        while (current):
            if prev.value == needle:
                self.head = current.next
                return

            if current.value == needle:
                prev.next = current.next
                return

            prev = current
            current = current.next

    def traverse(self):
        current = self.head

        if self.isEmpty():
            print('List is empty')
            return

        while (current):
            print(current.value)
            current = current.next

    def search(self, value):
        current = self.head
        while (current):
            if current.value == value:
                return current
            current = current.next
        return None

    def isEmpty(self):
        return self.head is None

    def length(self):
        current = self.head
        count = 0
        if self.isEmpty():
            return 0

        while (current):
            count += 1
            current = current.next

        return count


link = LinkedList()

link.prepend(5)
link.prepend(7)
link.prepend(15)
# link.prepend(12)
# link.prepend(32)
# link.prepend(43)

# link.delete(15)

# print(link.length())

link.insertBefore(5, 314)

# link.prepend(8)

# link.prepend(33)

# link.append(45)
# link.append(88)

link.traverse()
