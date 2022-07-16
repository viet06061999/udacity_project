 # -*- coding: utf-8 -*-
class Node:
  def __init__(self, key=None, value=None):
    self.key = key
    self.value = value
    self.next = None
    self.prev = None
  def __str__(self):
     
     return str(self.key)+"-"+str(self.value)+"-next:"+str(self.next.key if self.next != None else "none" )+"-pre:"+str(self.prev.key if self.prev != None else "none" )
#implementation of Doubly Linked List for the hash table
class LinkedList:
  def __init__(self):
    self.head = None
    self.tair = None
  
  #add or update a node, return 0 if node added and 1 if node updated
  def insert(self, key, value):
    node = Node(key, value) #create a node
    if self.head == None: #if list is empty insert a node at the start
      self.head = node
      self.tair = node
      return node
    else:
      node.prev = self.tair
      self.tair.next = node
      self.tair = node
      return node

  def traverse(self):
          node = self.head 
          while node != None:
              print(str(node)) # in ra dữ liệu
              node = node.next 
    
class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity #maximum size of the array of buckets
        self.length = 0 #length of inserted items
        self.key_map = {}
        self.data = LinkedList()

    def get(self, key):
        result = -1
        if(key in self.key_map):
            element = self.key_map[key]
            if element.next == None:
              return element.value
            if key == self.data.head.key:
                self.data.head = element.next
                element.next.prev = None
            else:    
                element.prev.next = element.next
                element.next.prev = element.prev

            element.next = None
            element.prev = self.data.tair    
            self.data.tair.next = element
            self.data.tair = element
            result = element.value
        return result

    def set(self, key, value):
        if len(self.key_map) >= self.capacity:
            tmp = self.data.head
            self.data.head = tmp.next
            if( tmp.key in self.key_map):
                self.key_map.pop(tmp.key, None)
        self.key_map[key]=self.data.insert(key, value)
    

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# # Test Case 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
our_cache.get(1)
our_cache.get(2)
our_cache.get(9)

our_cache.set(5, 5) 
our_cache.set(6, 6)
our_cache.set(7, 7) 
our_cache.set(8, 8)
our_cache.set(9,9) 
our_cache.set(10, 10)
print ("Pass" if our_cache.get(2)  == -1 else "Fail")      
# expected output: -1
print ("Pass" if our_cache.get(10)  == 10 else "Fail")      
# expected output: 10

# Test Case 2
our_cache2 = LRU_Cache(5)
print ("Pass" if our_cache2.get(9)  == -1 else "Fail")   
# expected output: -1  
# Test Case 3
our_cache3 = LRU_Cache(5)

our_cache3.set(1, 1);
our_cache3.set(2, 2);
our_cache3.set(3, 3);
our_cache3.set(4, 4);
our_cache3.get(1)
our_cache3.set(5, 5) 
our_cache3.set(6, 6)
our_cache3.set(7, 7)
print ("Pass" if our_cache3.get(3)  == -1 else "Fail")   
# expected value: -1
print ("Pass" if our_cache3.get(1)  == 1 else "Fail")   
# expected value: 1