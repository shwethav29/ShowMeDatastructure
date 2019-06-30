import sys
from collections import defaultdict

#create a dictionary with characters as key and frequency as the value
def get_frequencies(inputString):
    string_freq = defaultdict(int)
    for ch in inputString:
        string_freq[ch] = string_freq[ch]+1
    return string_freq

#add two nodes as the leaves of the parent node. Parent node is the sum of the frequencies of the child node.
def merge_nodes(left,right):
    sum = left.frequency + right.frequency
    parent = Node("*",sum)
    parent.left = left
    parent.right = right
    left.parent = parent
    right.parent = parent
    return parent

#create priority queue by ordering the nodes with the increasing order of the frequency
def create_priority_queue(data):
    string_freq = get_frequencies(data)
    min_heap = MinHeap(len(string_freq))

    for key, value in string_freq.items():
        min_heap.insert(Node(key, value))
    return min_heap

#encodes the data and returns the encoded byte string and the huffman tree
def huffman_encoding(data):
    huffman_tree = HuffmanTree()
    if(data==None or len(data)<1):
        return "",huffman_tree
    priorityQueue = create_priority_queue(data)
    while priorityQueue.size > 1:
        node_left = priorityQueue.extract_min()
        node_right = priorityQueue.extract_min()
        parent_node = merge_nodes(node_left,node_right)
        priorityQueue.insert(parent_node)

    root = priorityQueue.extract_min()
    huffman_tree.root = root

    huffman_tree.populate_character_code(huffman_tree.root,"")
    encodedData_list = list()

    for ch in data:
        encodedData_list.append(huffman_tree.character_code[ch])
    return "".join(encodedData_list) , huffman_tree

#decodes the encoded data from the byte string using the tree
def huffman_decoding(data,tree):
    next = tree.root
    decoded_list = list()
    for ch in data:
        if next != None:
            if ch == '0':
                next = next.left
            elif ch == '1':
                next = next.right
            if tree.is_leaf_node(next):
                decoded_list.append(next.character)
                next = tree.root
    return "".join(decoded_list)

#tree node
class Node(object):
    def __init__(self,character,frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None
        self.parent = None

    def __gt__(self, other):
        if hasattr(other,"frequency"):
            return self.frequency > other.frequency

    def __lt__(self, other):
        if hasattr(other,"frequency"):
            return self.frequency < other.frequency

class MinHeap(object):
    def __init__(self,capacity=10):
        self.array = [None for i in range(capacity)]
        self.size = 0

    def insert(self,node):
        index = self.size
        self.array[index] = node
        self.size +=1
        parent_index = index // 2
        while(parent_index != 0):
         if(self.array[index] < self.array[parent_index]):
             temp = self.array[parent_index]
             self.array[parent_index] = node
             self.array[index] = temp
             index = parent_index
             parent_index = index // 2
         else:
             break

    def extract_min(self):
        if(self.size < 1):
            return None
        min = self.array[0]
        self.size -=1
        if(self.size<1):
            return min
        self.array[0] = self.array[self.size]
        index=0
        while(index<=self.size):
            left_child = (2*index) + 1
            right_child = (2 * index)+2
            parent = index
            if(left_child >self.size or right_child>self.size):
                return min
            if(self.array[left_child] < self.array[right_child]):
                if(self.array[left_child]<self.array[parent]):
                    index = left_child
            else:
                if (self.array[right_child] < self.array[parent]):
                    index = right_child
            if(parent == index):
                break
            temp = self.array[parent]
            self.array[parent] = self.array[index]
            self.array[index]=temp
        return min


class HuffmanTree(object):
    def __init__(self,root=None):
        self.root = root
        self.character_code = dict()

    #recursively calls in DFS to populate a dictionary of characters with corresponding code
    #the exit condition for the recursion is if the node is a leaf
    def populate_character_code(self,node,code):
        #leaf
        if self.is_leaf_node(node):
            self.character_code[node.character] = code
            return

        #traverse left
        if(node.left != None):
            self.populate_character_code(node.left,code+"0")

        #traverse right
        if(node.right != None):
            self.populate_character_code(node.right,code+"1")

    def is_leaf_node(self,node):
        return (node.left == None and node.right == None)

def test_get_frequencies(inputData):
    result_dict = {'T': 1, 'h': 2, 'e': 2, ' ': 4, 'b': 1, 'i': 2, 'r': 2, 'd': 2, 's': 1, 't': 1, 'w': 1, 'o': 1}
    output = get_frequencies(inputData)
    if(result_dict == output):
        print("pass")
    else:
        print("fail")


def test_function(inputData):

    print("#################################################################################")
    size = 0
    if len(inputData) > 0:
        size = sys.getsizeof(inputData)
    print("The size of the data is: {}\n".format(size))
    print("The content of the data is: {}\n".format(inputData))

    encoded_string, tree = huffman_encoding(inputData)

    size = 0
    if len(encoded_string)>0:
        size = sys.getsizeof(int(encoded_string, base=2))
    print("The size of the encoded data is: {}\n".format(size))
    print("The content of the encoded data is: {}\n".format(encoded_string))

    decoded_string = huffman_decoding(encoded_string, tree)

    size = 0
    if len(encoded_string)>0:
        size = sys.getsizeof(int(encoded_string, base=2))

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_string)))
    print("The content of the decoded data is: {}\n".format(decoded_string))


test_get_frequencies("The bird is the word")

test_function("The bird is the word")
#0010010110011111010100011000111100101011111011010110011110110011011000
#The bird is the word

test_function("Everest 'traffic jam' survivor calls for tougher rules")
#1100100110111110011111110010010101011010010000110010001011011110101011100000011010100101110111100001100011011011011001111001011101000110000000011101010010011110010101000111000111001111000111111001011000001000011111110
#Everest 'traffic jam' survivor calls for tougher rules


test_function("")
#empty string


test_function("T")
#empty string and empty tree


#print(sys.getsizeof(int("", base=2)))