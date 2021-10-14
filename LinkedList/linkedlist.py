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
            self.length += 1
            return
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.length += 1
            return
        current = self.head
        while (current.next):
            current = current.next
        current.next = newNode
        self.length += 1

    def insertBefore(self, needle, value):
        newNode = newNode = Node(value)

        if self.isEmpty():
            print('List is empty')
            return

        if self.search(needle) is None:
            print('Needle not found')
            return

        if self.length == 1:
            newNode.next = self.head
            self.head = newNode
            return

        current = self.head
        prev = current
        while (current):
            if current.value == needle:
                prev.next = newNode
                newNode.next = current
                self.length += 1
                return

            prev = current
            current = current.next

        return True

    def delete(self, needle):
        if self.isEmpty():
            print('List is empty')
            return   

        current = self.head
        prev = current
        while (current):
            if prev.value == needle:
                self.head = current.next
                self.length -= 1
                return

            if current.value == needle:
                prev.next = current.next
                self.length -= 1
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
