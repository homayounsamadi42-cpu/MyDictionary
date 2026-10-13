class TrieNode:
    def __init__(self):
        self.children = {}
        self.exact_matches = set()  
        self.partial_matches = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def process_word(self, word):
    
        return word[::-1] if " " in word else word

    def insert(self, word):
        word = self.process_word(word)
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.partial_matches.add(word)
        
        node.exact_matches.add(word)  

    def search_prefix(self, prefix):
        
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        
        return list(node.exact_matches) + list(node.partial_matches - node.exact_matches)

