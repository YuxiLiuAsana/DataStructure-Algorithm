from sets import Set
class Trie(object):
    def __init__(self):
        self.root = {}
    def insert(self, word):
        cur = self.root
        for x in word:
            if x not in cur:
                cur[x]={}
            cur = cur[x]
        cur['#']='#'
    def search(self, word):
        cur = self.root
        for x in word:
            if x not in cur:
                return False
            cur = cur[x]
        if '#' in cur:
            return True
        else :
            return False       

    def startsWith(self, prefix):
        cur = self.root
        for x in prefix:
            if x not in cur:
                return False
            cur = cur[x]
        return True

class Solution(object):
    def __init__(self):
        self.trie = Trie()

    def findWordsHelper(self, i, j, curr, pre):
        """
        :param visited: the visited set(i,j)
        :param i: the i position
        :param j: the j position
        :param curr: the current dictionary
        :param word: the word
        :param k: the index for the word
        :return: List[str]
        """
        retList = Set()
        if self.board[i][j] in curr:
            if '#' in curr[self.board[i][j]]:
                retList.add(pre + self.board[i][j])
            v = self.board[i][j]
            self.board[i][j] ='*'
            if i > 0 and self.board[i-1][j] != '*':
                retList = retList.union(self.findWordsHelper(i-1,j,curr[v],pre+v))
            if i < len(self.board)-1 and self.board[i+1][j] != '*':
                retList = retList.union(self.findWordsHelper( i+ 1, j, curr[v], pre + v))
            if j > 0 and self.board[i][j-1] != '*':
                retList = retList.union(self.findWordsHelper(i,j-1,curr[v], pre + v))
            if j < len(self.board[0])-1 and self.board[i][j+1] != '*':
                retList = retList.union(self.findWordsHelper(i,j+1,curr[v], pre + v))
            self.board[i][j] = v
        return retList

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if(len(board) == 0): return []
        if(len(board[0]) == 0): return []

        for w in words:
            self.trie.insert(w)
        self.board = board

        curr = self.trie.root
        retList = Set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                tempList =self.findWordsHelper(i,j,self.trie.root,"")
                retList= retList.union( tempList)
        return list(retList)


if __name__ == '__main__':
    board = [["a","b"],["a","a"]]
    word = ["baa","aaa","aaba"]
    s = Solution()
    print(s.findWords(board,word))