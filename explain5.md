complete the notebook. Because i cant run note book then i implement Trie using dictionary in python. 
implement Trie and using recursive to find suffix and for loop with prefix to find node 
- method 1: insert node
for each char in word and insert new node to trie using dictionary
eficiency space is O(1), eficiency time is O(n) where n is length of word
- method 2: find node by prefix
for each char in prefix if char is children of node then return node
eficiency space is O(1), eficiency time is O(n) where n is length of prefix
- method 3: suffixes
using dfs to find suffixes, the entire trie is traversed
=> eficiency time is O(n) where n is number of node
in case node is root -> result include all node then eficiency space is O(n) where n is number of node

