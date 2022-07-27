class TrieNode:
    """A node in the trie structure"""

    def __init__(self, c):
        self.char = c
        self.is_end = False
        self.children = {}

    def suffixes(self, suffix=""):
        result = []
        if self.is_end:
           return [suffix + self.char]
        for child in self.children.values():
            result+=child.suffixes(suffix + child.char)
        return result    
    def __str__(self):
        return self.char+ ' :' + str(self.children)
     
class Trie(object):
    def __init__(self):
        self.root = TrieNode(c="")

    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root
    
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        # Mark the end of a word
        end_node = TrieNode("")
        end_node.is_end = True
        node.children[""] = end_node

    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node    


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

f('tr')

