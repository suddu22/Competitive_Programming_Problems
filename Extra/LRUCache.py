#https://www.kunxi.org/blog/2014/05/lru-cache-in-python/
import collections
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = collections.OrderedDict()

    # @return an integer
    def get(self, key):
        if key in self.table:
            pop = self.table.pop(key)
            self.table[key] = pop
            return pop
        else:
            return -1


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        n = len(self.table)

        if n >= self.capacity:
            if key not in self.table:
                self.table.popitem(last=False)
            else:
                self.table.pop(key)
        self.table[key] = value

# 6 2
l = LRUCache(2)
# S 2 1
l.set(2, 1)
# S 1 1
l.set(1, 1)
# S 2 3
l.set(2, 3)
# S 4 1
l.set(4, 1)
# G 1
print l.get(1)
# G 2
print l.get(2)
