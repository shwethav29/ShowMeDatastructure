class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    hashtable1= dict()
    hashtable2 = dict()
    current_node = llist_1.head
    union = LinkedList()
    while(current_node != None):
        if (current_node.value not in hashtable1):
            hashtable1[current_node.value] = current_node.value
            union.append(Node(current_node.value))
        current_node = current_node.next

    current_node = llist_2.head
    while(current_node != None):
        if(current_node.value not in hashtable1 and current_node.value not in hashtable2):
            hashtable2[current_node.value] = current_node.value
            union.append(Node(current_node.value))
        current_node = current_node.next

    return union

def intersection(llist_1, llist_2):
    hashtable1= dict()
    hashtable2 = dict()
    current_node = llist_1.head
    intersection = LinkedList()

    while(current_node != None):
        if (current_node.value not in hashtable1):
            hashtable1[current_node.value] = current_node
        current_node = current_node.next

    current_node = llist_2.head
    while(current_node != None):
        if(current_node.value in hashtable1 and current_node.value not in hashtable2):
            hashtable2[current_node.value] = current_node
            intersection.append(Node(current_node.value))
        current_node = current_node.next

    return intersection


def test_function(element_1,element_2):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)
    print ("union {0}".format(union(linked_list_1,linked_list_2)))
    print ("intersection {0}".format(intersection(linked_list_1,linked_list_2)))


test_function([3,2,4,35,6,65,6,4,3,21],[6,32,4,9,6,1,11,21,1])
#union 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
#intersection 6 -> 4 -> 21 ->

test_function([3,2,4,35,6,65,6,4,3,23],[1,7,8,9,11,21,1])
#union 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
#intersection

test_function([],[])
#union
#intersection

test_function([1],[1])
#union 1 ->
#intersection 1 ->

test_function([1],[2])
#union 1 -> 2 ->
#intersection

test_function([1],[])
#union 1 ->
#intersection

