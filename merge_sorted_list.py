class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self,node):
        if(self.head == None):
            self.head = node
            return
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = node
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

def merge_sorted_lists(l1,l2):
    merged_list = None
    if(l1.head == None):
        return l2
    if(l2.head == None):
        return l1
    small = None
    big = None
    if(l1.head.value <= l2.head.value):
        small = l1.head
        big = l2.head
        merged_list=l1
    else:
        small = l2.head
        big = l1.head
        merged_list = l2

    prev = None
    while(small != None and big !=None):
        if(small.value > big.value):
            temp = small
            small = big
            big = temp
        while(small != None and small.value <= big.value):
            prev = small
            small = small.next
        prev.next = big

    return merged_list



def reverse_list(list):
    cur = list.head
    if(cur is None):
        return list
    prev = None
    while(cur.next != None):
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    cur.next = prev
    list.head = cur
    return list




elements1 = [3,6,9]
elements2 = [1,2,3,4]

l1 = LinkedList()
for item in elements1:
    l1.append(Node(item))

l2 = LinkedList()
for item in elements2:
    l2.append(Node(item))

merged = merge_sorted_lists(l1,l2)
print(merged)
reverse = reverse_list(merged)
print(reverse)
reverse = reverse_list(LinkedList())
print(reverse)