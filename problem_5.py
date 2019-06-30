from time import gmtime
import hashlib
import time
class Block:


    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    #Creates hash of timestamp, data and previous_hash
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp)+str(self.data)+str(self.previous_hash)
        sha.update(hash_str.encode("'utf-8'"))
        return sha.hexdigest()

#Node object contains block and the reference to next block
class Node(object):
    def __init__(self,block=None):
        self.block = block
        self.next = None

#Linked list to append blocks.
#maintains head and tail as we are always appending to the list and reading from begining of the list.
class LinkedList(object):
    def __init__(self,node = None):
        self.head = node
        self.tail = node

    def append(self,node):
        if self.head  == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

#Given the previous black creates next block
def next_block(lastblock):
    time_stamp = time.gmtime()
    data = "We are going to encode this string of data!"
    return Block(time_stamp,data,lastblock.hash)

#creates first block in the blockchain
def create_genesis_block():
  return Block(time.gmtime(), "Genesis Block", "0")

#prints the data, hash of the block and the hash of previous block
def print_blockchain(blockchain):
    if (blockchain == None or blockchain.head == None):
        print ("Block chain is empty")
        return
    node = blockchain.head
    while(node!=None):
        print ("Block {0} has been added to the blockchain!".format(node.block.data))
        print ("Hash data {0} ".format(node.block.hash))
        print ("Previous Hash data {0}".format(node.block.previous_hash))
        node = node.next

#creates the blockchain given the number of blocks in the block chain
def create_block_chain(num_of_blocks):
    if(num_of_blocks<1):
        return None
    last_block = create_genesis_block()
    blockchain = LinkedList(Node(last_block))
    for i in range(1,num_of_blocks):
        block_to_add = next_block(last_block)
        blockchain.append(Node(block_to_add))
        last_block = block_to_add
    return blockchain

#testing block chain with
# 0 data
# with one block
# with 20 blocks
def test_blockchain():
    blockchain = create_block_chain(20)
    print_blockchain(blockchain)
    #print 20 blocks output with data, hash and previous hash. when previous hash is equal to has of previous block


    blockchain = create_block_chain(0)
    print_blockchain(blockchain)
    # Block chain is empty

    blockchain = create_block_chain(1)
    print_blockchain(blockchain)

    #Block Genesis Block has been added to the blockchain!
    #Hash data 892f9255127276e961a0d3e35f688948a926f6377f1840af4fb75aab41f47df4
    #Previous Hash data 0


test_blockchain()



test_blockchain();