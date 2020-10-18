
class WordDictionary(object):

    def __init__(self, c = ""):
        """
        Initialize your data structure here.
        """
        self.val = c
        self.children = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if word == "":
            self.children[""] = WordDictionary()
        else:
            w = word[0]
            if not w in self.children:
                self.children[w] = WordDictionary(w)
            self.children[w].addWord(word[1:])


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if word == "":
            return "" in self.children
        w = word[0]
        if w == ".":
            r = word[1:]
            for k, v in self.children.items():
                if v.search(r):
                    return True
            return False
        if w in self.children:
            return self.children[w].search(word[1:])
        else:
            return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)