class RouteTrieNode:
    def __init__(self, part):
        # Initialize the node with children as before, plus a handler
        self.part = part
        self.children = {}
        self.handler = None
        self.is_end = False

# The Router class will wrap the Trie and handle 
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode('/')
        self.root.handler = root_handler

    def insert(self, paths, handler):
        node = self.root
        list_path = paths.split('/')
        for part in list_path:
            if part in node.children:
                node = node.children[part]
            else:
                new_node = RouteTrieNode(part)
                node.children[part] = new_node
                node = new_node
        
        # Mark the end of a word
        end_node = node
        end_node.is_end = True
        end_node.handler = handler

    def find(self, path):
        node = self.root
        if path == '/':
            return self.root.handler
        list_path = path.split('/')
        for part in list_path:
            if part in node.children:
                node = node.children[part]
            else:
                return None
        return node.handler    

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class Router:
    def __init__(self, root_handler):
        self.trie = RouteTrie(root_handler)

    def add_handler(self, path, handler):
        self.trie.insert(path, handler)

    def lookup(self, path):
        return self.trie.find(path)


# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
