'''
 The generators are used to avoid the 'MemoryError' exception
 when large iterables are passed.
'''


# Example without class
def gen(n):
    if n >10:
        print('Number too big')
        raise StopIteration
    for i in range(n):
        yield i

ge = gen(5)

while True:
    try:
        print(next(ge))
    except StopIteration:
        print()
        break

# -----------------------------------
# -----------------------------------
# -----------------------------------

# Example with class
class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0
        if n >10:
            print('Number too big \n')
            raise StopIteration

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration

        rv = self.last ** 2
        self.last += 1
        return rv

g = Gen(5)

while True:
    try:
        print(next(g))
    except StopIteration:
        break
