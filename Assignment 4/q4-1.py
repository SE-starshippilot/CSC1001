class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0

    def insert(self, data):
        new = Node(data, self.head)
        new.pointer = self.head
        self.head = new

    def recursive_count(self, node):
        if node is not None:
            self.__size = 1 if node == self.head else self.__size + 1
            self.recursive_count(node.pointer)
        else:
            print(self.__size)
