#Constants:

SPACE_INDEX = 26
CHARACTER_NUM = 27

#Classes:

# Class Trie:

class TrieNode:
    """
    Trie node class
    """

    def __init__(self) -> None:
        
        self._children = [None]*CHARACTER_NUM
        """ _children contains an array for 26 letters and a ' ' chararcter(space), which is the last one."""
        self._is_end_of_word = False
        self._data =''

class Trie:
    """
    Trie data structure class.
    """

    def __init__(self) -> None:
        self._root = self.getNode()

    def getNode(self) -> TrieNode:
        """
        Returns new trie node (initialized to NULLs).
        """
        return TrieNode()

    def _charToIndex(self, ch: str) -> int:
        """
        Private helper function. Returns the index of a lower case character.
        """
        if ch == ' ':
            return SPACE_INDEX
        elif ord('a') <= ord(ch) <= ord('z'):
            return ord(ch) - ord('a')
        else:
            return -1

    def insert(self, key: str, data: str) -> None:
        """
        Inserts key into trie, if not presents.
        If the key is prefix of trie node, just marks leaf node.
        :param key: A key to insert. The key must be composed only of letters and a space between words.
        :param data: A string which will be in the leaf of the key.
        :return: None
        """
        key = key.lower().strip() #for now, we convert every key to lower case.
        current_node = self._root
        for letter in key:
            index = self._charToIndex(letter)
            if index == -1: # in case of illegal character:
                raise ValueError
            if not current_node._children[index]:
                current_node._children[index] = self.getNode()
            current_node = current_node._children[index]
        #mark the last node as a leaf:
        current_node._is_end_of_word = True
        current_node._data = data

    def find(self, key: str) -> str:
        """
        Searches the key in the trie.
        :param key: A key to search. The key must be composed only of letters and a space between words.
        :return: The data if key presents in trie. Else, the empty srting - ''.
        """
        key = key.lower().strip() #for now, we convert every key to lower case.
        current_node = self._root 
        for letter in key:
            index = self._charToIndex(letter)
            if not current_node._children[index]:
                return ''
            current_node = current_node._children[index]
        return current_node._data if current_node._is_end_of_word else ''    

# =====================================


# =====================================