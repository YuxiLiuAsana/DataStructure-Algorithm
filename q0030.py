class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        listLen = len(words)
        if listLen == 0: return []
        wordLen = len(words[0])
        if wordLen == 0: return []
        wordMap = {}
        for w in words:
            if not w in wordMap:
                wordMap[w] = 0
            wordMap[w] += 1
        ret = []
        for i in range(wordLen):
            tempMap = {}
            start = i
            for j in range(i, len(s), wordLen):
                if tempMap == wordMap:
                    ret += [j-wordLen * listLen]
                currentWord = s[j:j+wordLen]
                if not currentWord in wordMap:
                    tempMap = {}
                    start = j + wordLen
                else:
                    if not currentWord in tempMap:
                        tempMap[currentWord] = 0
                    tempMap[currentWord] += 1
                    while tempMap[currentWord] > wordMap[currentWord]:
                        tempMap[s[start:start+wordLen]] -=1
                        start = start + wordLen
            if tempMap == wordMap: 
                ret += [j - wordLen * (listLen-1)]
        return ret
                
        
      
