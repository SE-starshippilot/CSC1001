class Stack:
    def __init__(self):
        self.__content = []

    def push(self, val):
        self.__content.append(val)

    def pop(self):
        tmp = None
        if self.notEmpty():
            tmp = self.__content[-1]
            del self.__content[-1]
        return tmp

    def top(self):
        return self.__content[-1] if self.notEmpty else None

    def __len__(self):
        return len(self.__content)

    def notEmpty(self):
        return True if len(self) else False


HTstack = Stack()


def HanoiTower(n):
    global HTstack
    HTstack.push([n, ['A', 'B', 'C']])
    while HTstack.notEmpty():
        tmp = HTstack.pop()
        HTstack.push([tmp[0]-1, tmp[1][1::-1]+tmp[1][-1:-2:-1]])
        HTstack.push([1, tmp[1]])
        HTstack.push([tmp[0]-1, tmp[1][0:1]+tmp[1][:0:-1]])
        while HTstack.notEmpty() and HTstack.top()[0] == 1:
            move = HTstack.pop()[1]
            move[1] = '->'
            print(' '.join(move))
