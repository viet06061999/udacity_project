 # -*- coding: utf-8 -*-
import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
    def __str__(self):
        return str(self.previous_hash) + "-" + self.data

    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = str(self).encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()  
class LinkedList:
  def __init__(self):
    self.head = None
    self.tair = None
    self.map_table = {}

  def insert(self, data):
    block = Block(datetime.now(), data, self.tair.hash if self.tair!=None else "0") 
    self.map_table[block.hash] = block
    if self.head == None: 
      self.head = block
      self.tair = block
      return block
    else:
      block.previous_hash = self.tair.hash if self.tair!=None else None
      self.tair = block
      return block

  def traverse(self):
          block = self.tair 
          while block != None:
              print(str(block)) # in ra dữ liệu
              block = self.map_table[block.previous_hash] if block.previous_hash  != "0" else None


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# # Test Case 1
blocks = LinkedList()
blocks.insert("1")
blocks.insert("2")
blocks.insert("3")
blocks.insert("4")
blocks.traverse()
# expected result:
# 8b23119ee76ff83e72a9e73196ebd4862ab242bb6f45597f2a384ff7654b9f41-4
# 39d254fbe01a222e40afca3e714bf333bdf447a342729c61a7f8ac009f8d24fe-3
# 389f7fbc8e058d61efa91d591e1dc5c5ad418fec3fb2d4aa68ec49ae4e7b784e-2
# 0-1
# # Test Case 2
blocks1 = LinkedList()
blocks.traverse()
# expected result: empty list
# # Test Case 3
blocks2 = LinkedList()
blocks2.insert("1")
blocks2.insert("2")
blocks2.insert("3")
blocks2.traverse()
# expected result:
# 39d254fbe01a222e40afca3e714bf333bdf447a342729c61a7f8ac009f8d24fe-3
# 389f7fbc8e058d61efa91d591e1dc5c5ad418fec3fb2d4aa68ec49ae4e7b784e-2
# 0-1
