class A:
    def __init__(self):
        self.a = [1, 3, 2, 4, 5]

    def get(self):
        return self.a

    def set(self):
        ls = self.a
        srt(ls)

    def srt(self, lst):
        lst.sort()
        return lst
    
    def __str__(self):
        a.set()
        return str(self.a)


a = A()
print(a)
