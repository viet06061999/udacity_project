from collections import Counter
import sys


class NodeTree(object):
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data

    def children(self):
        return self.left, self.right

    def __str__(self):
        return self.left, self.right, self.data


def huffman_code_tree(node, binString=''):
    '''
    Function to find Huffman Code
    '''
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, binString + '0'))
    d.update(huffman_code_tree(r, binString + '1'))
    return d


def make_tree(nodes):
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        if(c1 == c2):
            tmp = key2
            key2 = key1
            key1 = tmp
        node = NodeTree(key1, key2, c1+c2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes[0][0]

def huffman_encoding(data):
    freq = dict(Counter(data))
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    node = make_tree(freq)
    encoding = huffman_code_tree(node)
    result = ''
    for i in data:
       result += encoding[i]
    return result, node   
    
def huffman_decoding(encodedData,tree):
    treeHead = tree  
    decodedOutput = []  
    for x in encodedData:  
        if x == '1':  
            tree = tree.right     
        elif x == '0':  
            tree = tree.left  
        try:  
            if tree.children == None:  
                pass  
        except AttributeError:  
            decodedOutput.append(tree)  
            tree = treeHead  
          
    string = ''.join([str(item) for item in decodedOutput])  
    return string  

def test(testcase):
    if testcase == None or len(testcase)==0:
        print("null")
        return
    codes = {}

    a_great_sentence = testcase

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Test Case 1
test("")
# expected output: null
# Test Case 2
test(None)
# expected output: null
# Test Case 3
test("The bird is the word")
# expected output:1100100101010110100001110011100001100010111110010101011110110111110011
