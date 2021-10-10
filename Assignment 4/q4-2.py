class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def insert(self, data):
        new = Node(data, self.head)
        new.pointer = self.head
        if self.__size == 0:
            self.tail = new
        self.head = new
        self.__size += 1

    def quick_sort(self, node):
        if self.__size <= 1:
            return self.head
        left = SinglyLinkedList()
        key = node.element
        p = node
        q = node.pointer
        while q is not None:
            if q.element > key:
                p = q
                q = q.pointer
            else:
                left.insert(self.remove(q, p))
                q = p.pointer
        self.remove(self.head)
        if left.head is not None:
            left.quick_sort(left.head)
        left.append(key)
        self.head = self.quick_sort(self.head)
        self.concat(left)
        return self.head

    def remove(self, q, p=None):
        if self.__size > 1:
            if q is not self.head:
                p.pointer = q.pointer
                q.pointer = None
                if q is self.tail:
                    self.tail = p
            else:
                self.head = q.pointer
            self.__size -= 1
            return q.element
        else:
            self.head = self.tail = None
            self.__size -= 1

    def concat(self, other):
        if other.head is not None:
            other.tail.pointer = self.head
            self.head = other.head
            self.tail = other.tail
            self.__size += len(other)
        return self

    def append(self, data):
        new = Node(data, None)
        if self.__size == 0:
            self.head = self.tail = new
        else:
            self.tail.pointer = new
            self.tail = new
        self.__size += 1

    def __len__(self):
        return self.__size

    def out(self, node):
        while node is not None:
            print(node.element)
            node = node.pointer
