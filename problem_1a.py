class Node(object):
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class Double_LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, node):
        # if it is first node in the list
        if self.head is None:
            node.next = None
            node.prev = None
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node

    def move_node_to_end(self, node):
        # if node is the last node then it is already in right position
        if (self.tail == node):
            return
        self.remove(node)
        self.append(node)

    def remove(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        if (node.prev != None):
            node.prev.next = node.next
        if (node.next != None):
            node.next.prev = node.prev


class LRU_Cache(object):

    def __init__(self, capacity=5):
        # cache size
        self.csize = capacity
        # dictionary for key and node reference
        self.hashtable = dict()
        self.d_list = Double_LinkedList()

    def get(self, key):
        # Retrieve item from cache with key. Return -1 if nonexistent.
        if key in self.hashtable:
            node = self.hashtable[key]
            value = node.value
            # update cache for least recently accessed element
            self.update_cache(node)
            return value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is full remove the oldest item.
        if key not in self.hashtable:
            if len(self.hashtable) == self.csize:
                oldest_node = self.d_list.head
                oldest_key = oldest_node.key
                self.d_list.remove(oldest_node)
                del self.hashtable[oldest_key]
            node = Node(key, value)
            self.d_list.append(node)
            self.hashtable[key] = node
        else:
            node = self.hashtable[key]
            node.value = value
            self.get(key)

    # update the cache for least recently accessed element
    def update_cache(self, node):
        self.d_list.move_node_to_end(node)
        self.hashtable[node.key] = node


# test when cache is empty
def test_function1():
    our_cache = LRU_Cache(5)
    output = our_cache.get(1)
    if output == -1:
        print("Pass")
    else:
        print("Fail")


# test when cache has just one element and then get that element
def test_function2():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    output = our_cache.get(1)
    if output == 1:
        print("Pass")
    else:
        print("Fail")


# test when cache is full and we insert a new element. This should remove the least recently accessed element
# insert 1,2,3,4,5 when we insert 6 it should remove element with key=1 and insert 6
def test_function3():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    output = our_cache.get(1)
    if output == -1:
        print("Pass")
    else:
        print("Fail")


# insert elements 1,2,3,4,5 then do get key=1. Now least recently accessed element is 2 as we just read 1.
# Now when we insert 6 it should remove element key =2
def test_function4():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    # do a get call so key=1 will be most recently accessed
    output = our_cache.get(1)
    our_cache.set(6, 6)
    output = our_cache.get(2)
    if output == -1:
        print("Pass")
    else:
        print("Fail")


# setting the key which is already in cache. This should just update the cache least recently accessed
def test_function5():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    our_cache.set(1, 1)
    output = our_cache.get(2)
    if output == 2:
        print("Pass")
    else:
        print("Fail")


def test_function6():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(1, 4)
    output = our_cache.get(1)
    if output == 4:
        print("Pass")
    else:
        print("Fail")


test_function1()
test_function2()
test_function3()
test_function4()
test_function5()
test_function6()
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(1)  # returns -1
our_cache.get(2)  # returns 2
our_cache.get(3)  # return -1