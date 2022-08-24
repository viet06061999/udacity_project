implement same Trie. Only diference is save a handler for a node and instead of char it's part

- method 1: insert node
for each part in path and insert new node to trie using dictionary
eficiency space is O(1), eficiency time is O(n) where n is length of parts
- method 2: find node by path
for each part in path if part is children of node then return chidren of node 
eficiency space is O(1), eficiency time is O(n) where n is length of prefix
