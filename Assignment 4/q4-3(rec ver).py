stack = Stack()


class Stack:
    def __init__(self):
        self.content = []
        self.size = 0

    def push(self, val):
        self.content.append(val)
        self.size += 1

    def pop(self):
        if self.size != 0:
            self.size -= 1
            return self.content.pop()


def hn(n):
    step1 = Stack()
    st = ['A','B','C']
    for k in range(n, 1, -1):
        step1.push(st[1])
        step2.push(st[2])
        st = st[0] + st[:0:-1]
    for k in range(n, 1, -1):
        ans1.append(st[0],'->',step1.pop())

